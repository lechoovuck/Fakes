from django.shortcuts import render
from django.http import JsonResponse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import requests as rqs
from scanner.models import MalwareSite  
from crawler.views import crawl  
from . import site_parser 


apikey =  '1cb707fbec13a7d78994c7f3489f2c261dcb328e1d0cf9c21e2c2287e528ba8e'

def is_ajax(request):
     return request.headers.get('x-requested-with') == 'XMLHttpRequest'

def is_valid_url(url):
    validate = URLValidator()
    try:
        validate(url) # check if url format is valid
    except ValidationError:
        return False
    return True


def malurl_form(request):
    if request.method == 'POST':
        geturl = request.POST.get("siteurl", "")  
        
        site_parser.parse_links(geturl) 
        
        site_domain = geturl.split('/')[2]
        
        registered = MalwareSite.objects.filter(url = site_domain, malicious = True)
           
        apiresponse = "https://www.virustotal.com/vtapi/v2/url/report?apikey=" + apikey + "&resource=" + geturl
        response = rqs.get(apiresponse).json()    
         
        if response['response_code'] == 0 or not is_valid_url(geturl):
            message = 'Неверный адрес. Проверьте формат (https://example.com)'
            level = 0
        else:            
            new_record = MalwareSite(url = site_domain)     

            imprint = response['positives']
            if imprint==1 or registered:
                message="Сайт может быть вредоносным, "+str(imprint)+ "1 база данных отметила его как содержащий угрозу."
                level = 1
            elif imprint >1:
                message="Сайт является вредоносным, "+str(imprint)+" баз(ы) данных отметили его как содержащий угрозу"
                level = 2
                new_record.malicious = True
            else:
                message="Сайт не содержит угроз."
                level = 3
                
            if not MalwareSite.objects.filter(url = site_domain).exists():
                new_record.save()
        if is_ajax(request):
            return crawl(request, {'msg': message, 'level': level, 'response_code': response['response_code']})
        

    return render(request, "home/index.html", {
        'obj': 'Домашняя страница',
        'home': True,
        'check': False,
        'useful': False,
        'tested': False
        })
    
def useful(request):
    return render(request, "home/useful.html", {
        'obj': 'Полезная информация',
        'home': False,
        'check': False,
        'useful': True,
        'tested': False
        })
    



