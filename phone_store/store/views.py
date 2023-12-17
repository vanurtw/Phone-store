from django.shortcuts import render
from .models import PhoneProduct


# Create your views here.


def home_page(request):
    products = PhoneProduct.published.all()[:4]
    return render(request, 'store/home.html', {'products': products})


def shop_page(request):
    context = {}
    products = PhoneProduct.published.all()
    context['products'] = products
    return render(request, 'store/shop.html', context)
