from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.malurl_form, name='index'),
    path("useful-info", views.useful, name="useful-info")
]
