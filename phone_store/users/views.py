from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm


# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if not user is None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Проверте правильность полей')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', context={'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')
