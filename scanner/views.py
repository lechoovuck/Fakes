from django.shortcuts import render
import requests as rqs
from crawler.views import crawl

from .models import MalwareSite    

def pull_malware_sites(request):
    response = rqs.get('https://domains-monitor.com/api/v1/2b9cd3b55746a282c74b7b0d5cd483c0/malware/json/').json()
    malware_urls = response["domain"]
    for malware_url in malware_urls:
        if not MalwareSite.objects.filter(url = malware_url).exists():
            MalwareSite(url = malware_url, malicious=True).save()
    crawl(request, {})
    return get_malware(request)
        
def get_malware(request):
    all_sites = MalwareSite.objects.all().order_by('id')

    return render(request, "scanner/tested.html", {
        'obj': 'Проверенные сайты',
        'home': False,
        'check': False,
        'useful': False,
        'tested': True,
        'all_sites': all_sites
        })
