"""
URL configuration for cactus project.
The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import include, path

import sources.account.urls as account
import sources.home.urls as home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(home)),
    path("account/", include(account)),
]
