from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="project_home"),
]
