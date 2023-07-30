from django.contrib import admin
from django.urls import path
import home.views as home

urlpatterns = [
    path("", home.home, name="main_home"),
]
