from django.shortcuts import render
import requests as rqs


def get_api(request):
    response = rqs.get()