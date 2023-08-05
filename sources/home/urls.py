from django.urls import path

import sources.home.views as home

urlpatterns = [
    path("", home.home, name="main_home"),
]
