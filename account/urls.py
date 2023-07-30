from django.urls import path
import account.views as account

urlpatterns = [
    path("", account.home, name="account_home"),
    path("login/", account.login, name="account_login"),
]
