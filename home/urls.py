from django.urls import path, include
from django.conf.urls import handler500

handler500 = 'home.views.error_500'
handler404 = 'home.views.error_404'

from . import views

urlpatterns = [
    path("", views.malurl_form, name='index'),
    path("useful-info", views.useful, name="useful-info")
]
