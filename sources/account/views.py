from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import CreateAccount, Login

# pylint: disable = W0511,C0209


# Create your views here.
def home(request):
    return render(request, template_name="account/account.html")


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

            # if not user:
            #     return render(
            #         request,
            #         template_name="account/create_account.html",
            #         context={
            #             "create_account": create_account_form,
            #             "login_error": True,
            #         },
            #     )

    create_account_form = CreateAccount()

    return render(
        request,
        template_name="account/create_account.html",
        context={"create_account": create_account_form},
    )
