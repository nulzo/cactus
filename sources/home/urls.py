import home.views as home
from django.urls import path

urlpatterns = [
    path("", home.home, name="main_home"),
]
