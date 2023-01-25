from uuid import uuid4
from urllib.parse import urlparse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from scrapyd_api import ScrapydAPI
from .models import ScrapyItem

# connect scrapyd service
scrapyd = ScrapydAPI('http://localhost:6800')


def is_valid_url(url):
    validate = URLValidator()
    try:
        validate(url) 
    except ValidationError:
        return False

    return True


@csrf_exempt
@require_http_methods(['POST', 'GET'])
def crawl(request, json_dict):
    endresponse = dict()
    if request.method == 'POST':
        url = request.POST.get('siteurl', None)

        if not url:
            endresponse['error'] = 'Missing  args'
        elif not is_valid_url(url):
            endresponse['error'] = 'URL is invalid'

        domain = urlparse(url).netloc
        start_url = url.split('/')[2]
        
        print(start_url)
        
        if not ScrapyItem.objects.filter(start_url=start_url).exists():
            unique_id = str(uuid4())
            
            settings = {
                'unique_id': unique_id,
                'start_url': start_url,
                'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
            }

            
            task = scrapyd.schedule('default', 'scraper', 
                settings=settings, url=url, domain=domain)
            endresponse.update({'task_id': task, 'unique_id': unique_id, 'status': 'started', 'start_url': start_url })

    elif request.method == 'GET':
        task_id = request.GET.get('task_id', None)
        unique_id = request.GET.get('unique_id', None)
        start_url = request.GET.get('start_url', None)

        if not task_id or not unique_id:
            endresponse.update({'error': 'Missing args'})

        status = scrapyd.job_status('default', task_id)
        if status == 'finished':
            try:
                item = ScrapyItem.objects.get(start_url=start_url) 
                endresponse.update({'data': item.to_dict['data']})
            except Exception as e:
                endresponse.update({'error': str(e)})
        else:
            endresponse.update({'status': status})
    return JsonResponse(dict(endresponse, **json_dict))