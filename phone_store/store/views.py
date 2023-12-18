from django.shortcuts import render
from .models import PhoneProduct
from cart.cart import Cart
from django.http import HttpResponse


# Create your views here.


def home_page(request):
    products = PhoneProduct.published.all()[:4]
    return render(request, 'store/home.html', {'products': products})


def shop_page(request):
    context = {'chapter': 'shop'}
    context['type_product'] = request.GET.get('type-product', None)
    if context['type_product'] == 'laptop':
        products = []
    elif context['type_product'] == 'iphone':
        products = PhoneProduct.published.all()
    else:
        products = PhoneProduct.published.all()
    context['products'] = products
    return render(request, 'store/shop.html', context)


def aaa(request):
    cart = Cart(request)
    pr = PhoneProduct.objects.all()[0]
    cart.get_total_price()
    return HttpResponse('awdwa')
