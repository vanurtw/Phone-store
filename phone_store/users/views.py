from django.contrib.auth import login, authenticate
from django.shortcuts import render
from .forms import RegisterForm


# Create your views here.

def register_user(request):
    form = RegisterForm
    return render(request, 'user/login-register.html', context={'form':form})

# def login_user(request):
#     login(request)