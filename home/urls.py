from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("check-page", views.check, name="check-page"),
    path("tested-sites", views.tested, name="tested-sites"),
    path("useful-info", views.useful, name="useful-info"),
    path('', include("scanner.urls"))
]
