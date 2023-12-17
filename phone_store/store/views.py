from django.shortcuts import render
from .models import PhoneProduct


# Create your views here.


def home_page(request):
    phones = PhoneProduct.published.all()[:4]
    return render(request, 'store/home.html', {'phones': phones})
