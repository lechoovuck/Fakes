from django.shortcuts import render
from django.http import JsonResponse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import requests as rqs
from scanner.models import MalwareSite    


apikey =  '1cb707fbec13a7d78994c7f3489f2c261dcb328e1d0cf9c21e2c2287e528ba8e'

def is_ajax(request):
     return request.headers.get('x-requested-with') == 'XMLHttpRequest'

def error_500(request,exception=None):
    return render(request, "urlerror.html", {})
    
def error_404(request,exception=None):
    return render(request, "urlerror.html", {})

def is_not_valid_url(url):
    validate = URLValidator()
    try:
        validate(url)
        return False
    except ValidationError:
        return True 


def malurl_form(request):
    if request.method == 'POST':
        geturl = request.POST.get("siteurl", "")            
        apiresponse = "https://www.virustotal.com/vtapi/v2/url/report?apikey=" + apikey + "&resource=" + geturl
        response = rqs.get(apiresponse).json()    
         
        if response['response_code'] == 0:
            message = 'Неверный адрес'
            level = 0
        else:
            imprint = response['positives']
            if imprint==1:
                message="Сайт может быть вредоносным, "+str(imprint)+ " база данных отметила его как содержащий угрозу."
                level = 1
            elif imprint>1:
                message="Сайт является вредоносным, "+str(imprint)+" баз данных отметили его как содержащий угрозу"
                level = 2
                
                malware_site_data = MalwareSite(
                    url = geturl
                )
                malware_site_data.save()
            else:
                message="Сайт не содержит угроз."
                level = 3
            
        if is_ajax(request):
            return JsonResponse({'msg': message, 'level': level})

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
    



