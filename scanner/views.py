from django.shortcuts import render, redirect
import requests as rqs

import pandas as pd

import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn import metrics
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns   
from sklearn.tree import export_graphviz

from .models import MalwareSite    

def pull_malware_sites(request):
    response = rqs.get('https://domains-monitor.com/api/v1/2b9cd3b55746a282c74b7b0d5cd483c0/malware/json/').json()
    
    malware_urls = response["domain"]

    for i in malware_urls:
        malware_site_data = MalwareSite(
            url = i
        )
        malware_site_data.save()
    
    return redirect('', request)
    

def get_api(request):
    response = rqs.get('https://domains-monitor.com/api/v1/2b9cd3b55746a282c74b7b0d5cd483c0/get/ru/list/text/')
    
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
