from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.get_malware, name="tested-sites"),
    path("#", views.pull_malware_sites, name="pull-malware-sites"),
]
