from django.contrib.auth.forms import AuthenticationForm
from django import forms


class EmailRegistrationForm(forms.Form):
    recipient = forms.EmailField(label='Email')


class LoginForm(forms.Form):
    user_name = forms.CharField(label='User Name', max_length=50)
    password = forms.PasswordInput()


class QuickStartSearchForm(forms.Form):
    organization = forms.CharField(label='Organization', max_length=100)
    election_date = forms.DateField(label='Election Date')


class OrganizationSearchForm(forms.Form):
    organization = forms.CharField(label='Organization', max_length=100)
