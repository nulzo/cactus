import account.views as account
from django.urls import path

urlpatterns = [
    path("", account.home, name="account_home"),
    path("login/", account.login, name="account_login"),
    path("create-account/", account.create_account, name="account_create"),
]
