from django.shortcuts import render, redirect
from .forms import ExampleForm


# Create your views here.
def home(request):
    return render(request, template_name="account/account.html")


def login(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        example_form = ExampleForm(request.POST)
        # check whether it's valid:
        if example_form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, template_name="account/login.html", context={"example_form": example_form})

    example_form = ExampleForm()

    return render(request, template_name="account/login.html", context={"example_form": example_form})
