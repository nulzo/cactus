from django.urls import path
import account.views as account
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", account.home, name="account_home"),
    path('login/', account.login, name='account_login'),
    path('create-account/', account.create_account, name='account_create'),
]