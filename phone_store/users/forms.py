from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            forms.ValidationError('Пароли не совпадают!')
        return cd['password']


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'sin-login-register', 'placeholder': "User name or email address *"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'sin-login-register', 'placeholder': "Password *"}))
