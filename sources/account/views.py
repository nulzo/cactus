import datetime

import numpy as np
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from sources.account.models import daily_spending, user_account

from .forms import CreateAccount, Login

# pylint: disable = W0511,C0209,E1101


# Create your views here.
def home(request):
    username: user_account.UserAccount = user_account.UserAccount.objects.all().first()
    spending: daily_spending.DailySpending = username.daily.all().first()

    year = 2023
    month = 8
    my_date = datetime.date(year, month, 1)
    delta = datetime.timedelta(days=1)
    dates = []

    while my_date.month == month:
        dates.append(my_date.strftime("%d-%b-%Y"))
        my_date += delta

    ids = list(spending.__dict__.keys())[3:-1]
    # data = list(spending.__dict__.values())[3:-1]
    vals = np.random.rand(50, 50).tolist()
    print(vals)
    context = {"id": ids, "data": vals, "dates": dates}
    return render(request, context=context, template_name="account/account.html")


def logout_page(request):
    logout(request)
    messages.success(request=request, message="You have been logged out. See ya soon!")
    return redirect("account_login")


def login_page(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request
        login_form = Login(request.POST)
        # check whether it's valid:
        if login_form.is_valid():
            password = request.POST.get("password")
            username = request.POST.get("email")
            if not password or not username:
                errors = {"Invalid Entry": "Please ensure the entries are valid!"}
                return render(
                    request,
                    template_name="account/login.html",
                    context={"login": login_form, "errors": errors},
                )

            user = authenticate(username=username, password=password)

            if not user:
                errors = {
                    "Username or Password not found": """
                    Erm... you aren't on our list
                    ... who do you even know here?
                    """
                }
                return render(
                    request,
                    template_name="account/login.html",
                    context={"login": login_form, "errors": errors},
                )

            login(request, user)
            return redirect("account_home")

    login_form = Login()

    return render(
        request,
        template_name="account/login.html",
        context={"login": login_form},
    )


def create_account(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request
        create_account_form = CreateAccount(request.POST)
        # check whether it's valid
        if create_account_form.is_valid():
            password = request.POST.get("password")
            reentered_password = request.POST.get("confirm_password")
            email = request.POST.get("email")
            username = request.POST.get("username")

            if password != reentered_password:
                errors = {
                    "Passwords did not match": "Please ensure the passwords entered match!"
                }
                return render(
                    request,
                    template_name="account/create_account.html",
                    context={"create_account": create_account_form, "errors": errors},
                )

            if not password or not username or not reentered_password:
                errors = {"Invalid Entry": "Please ensure the entries are valid!"}
                return render(
                    request,
                    template_name="account/create_account.html",
                    context={"create_account": create_account_form, "errors": errors},
                )

            user = authenticate(username=username, password=password)

            # TODO: login user if they exist

            if not user:
                new_user = User.objects.create_user(
                    username=username, password=password, email=email
                )
                login(request=request, user=new_user)
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Welcome, %s! You have been added to our database!"
                    % new_user.username,
                )
                return redirect("main_home")

    create_account_form = CreateAccount()

    return render(
        request,
        template_name="account/create_account.html",
        context={"create_account": create_account_form},
    )
