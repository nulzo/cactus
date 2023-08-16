from django.urls import path

import sources.account.views as account

urlpatterns = [
    path("", account.login_page, name="account_home"),
    path("login/", account.login_page, name="account_login"),
    path("create-account/", account.create_account, name="account_create"),
    path("logout/", account.logout_page, name="account_logout"),
]
