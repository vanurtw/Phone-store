from django.contrib.auth import login, authenticate
from django.shortcuts import render
from .forms import RegisterForm, LoginForm


# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = LoginForm()
    return render(request, 'user/login.html', context={'form':form})

# def login_user(request):
#     login(request)