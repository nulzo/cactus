from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, MultiField, Div, Field
from django import forms


class ExampleForm(forms.Form):

    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username', 'class': 'bold-font input-padding'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'password', 'class': 'input-padding'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'bold-font input-padding', 'placeholder': 'password'})
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field('email', data_name="whatever", autocomplete='off'),
            Field('password', data_name="whatever"),
        )
