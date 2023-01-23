
from django.shortcuts import render

def index(request):
    return render(request, "home/index.html", {
        'obj': 'Домашняя страница',
        'home': True,
        'check': False,
        'useful': False,
        'tested': False
        })

def check(request):
    return render(request, "home/check_page.html", {
        'obj': 'Проверка сайта',
        'home': False,
        'check': True,
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
    
def tested(request):
    return render(request, "home/tested.html", {
        'obj': 'Проверенные сайты',
        'home': False,
        'check': False,
        'useful': False,
        'tested': True
        })



