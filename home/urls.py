from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("check-page", views.check, name="check-page"),
    path("useful-info", views.useful, name="useful-info")
]
