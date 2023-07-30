from django.shortcuts import render, redirect
from .forms import Login, CreateAccount
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.
def home(request):
    return render(request, template_name="account/account.html")


def login(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request
        login_form = Login(request.POST)
        # check whether it's valid:
        if login_form.is_valid():
            password = request.POST.get("password")
            username = request.POST.get("email")
            if not password or not username:
                return render(request, template_name="account/login.html", context={"example_form": login_form, })
            user = authenticate(username=username, password=password)
            if not user:
                return render(request, template_name="account/login.html", context={"example_form": login_form, "login_error": True})

    login_form = Login()

    return render(request, template_name="account/login.html", context={"example_form": login_form})


def create_account(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request
        create_account_form = CreateAccount(request.POST)
        # check whether it's valid:
        if create_account_form.is_valid():
            password = request.POST.get("password")
            username = request.POST.get("email")
            if not password or not username:
                return render(request, template_name="account/create_account.html", context={"create_account": create_account_form})
            user = authenticate(username=username, password=password)
            if not user:
                return render(request, template_name="account/create_account.html",
                              context={"create_account": create_account_form, "login_error": True})

    create_account_form = CreateAccount()

    return render(request, template_name="account/create_account.html", context={"create_account": create_account_form})
