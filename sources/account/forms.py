from crispy_forms.bootstrap import StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout
from django import forms


class Login(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "username", "class": "bold-font input-padding"}
        )
    )
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "password", "class": "input-padding"}
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget = forms.PasswordInput(
            attrs={"class": "bold-font input-padding", "placeholder": "password"}
        )
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field("email", data_name="whatever", autocomplete="off"),
            Field("password", data_name="whatever"),
            StrictButton(
                "login",
                "submit",
                type="submit",
                css_class="custom-btn btn-green mt-5 mb-3 d-flex justify-content-center w-100",
            ),
        )


class CreateAccount(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "username", "class": "bold-font input-padding"}
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "username", "class": "bold-font input-padding"}
        )
    )
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "password", "class": "bold-font input-padding"}
        )
    )
    confirm_password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "reenter password",
                "class": "bold-font input-padding",
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget = forms.PasswordInput(
            attrs={"class": "bold-font input-padding", "placeholder": "password"}
        )
        self.fields["confirm_password"].widget = forms.PasswordInput(
            attrs={
                "class": "bold-font input-padding",
                "placeholder": "confirm password",
            }
        )
        self.fields["email"].widget = forms.TextInput(
            attrs={"class": "bold-font input-padding", "placeholder": "email"}
        )
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field("username", data_name="whatever", autocomplete="off"),
            Field("email", data_name="whatever", autocomplete="off"),
            Field("password", data_name="whatever"),
            Field("confirm_password", data_name="whatever"),
            StrictButton(
                "create account",
                "submit",
                type="submit",
                css_class="custom-btn btn-green mt-5 mb-3 d-flex justify-content-center w-100",
            ),
        )
