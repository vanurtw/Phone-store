from django import forms
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'sin-login-register', 'placeholder': "User name or email address *"}))
    password = forms.CharField(min_length=7,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'sin-login-register', 'placeholder': "Password"}))
    password2 = forms.CharField(min_length=7,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'sin-login-register', 'placeholder': "Password repeat"}))

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(Q(username=cd['username']) | Q(email=cd['username'])):
            raise forms.ValidationError('Пользователь с таким именем уже есть')
        return cd['username']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cd['password']


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'sin-login-register', 'placeholder': "User name or email address *"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'sin-login-register', 'placeholder': "Password *"}))


class PasswordResetFormUser(PasswordResetForm):
    email = forms.EmailField(label='email', max_length=254, widget=forms.EmailInput(
        attrs={'class': 'sin-login-register', 'placeholder': "Enter linked to account email"}))


class SetPasswordFormUser(SetPasswordForm):
    new_password1 = forms.CharField(label='New password',
                                    widget=forms.PasswordInput(attrs={'class': 'sin-login-register',
                                                                      'placeholder': 'Enter a new password'}))
    new_password2 = forms.CharField(label='Repeat new password',
                                    widget=forms.PasswordInput(attrs={'class': 'sin-login-register',
                                                                      'placeholder': 'Repeat new password'}))
