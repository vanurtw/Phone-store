from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from cart.cart import Cart
from store.models import PhoneProduct, ColorCountProduct
from .models import Coupon
from django.utils import timezone
from django.contrib import messages


# Create your views here.
def cart(request):
    contex = {'chapter': 'None'}
    cart = Cart(request)
    if cart:
        return render(request, 'cart/cart.html', context=contex)
    return render(request, 'cart/empty-cart.html', context=contex)


def add_cart(request, id, slug):
    cart = Cart(request)
    if request.method == 'POST':
        color = request.GET.get('color')
        memory = request.GET.get('memory')
        quantity = request.POST.get('quantity')
        product = PhoneProduct.objects.get(id=id).colors.get(color=color.upper(), memory=memory)
        cart.add(product, quantity=int(quantity))
    else:
        product = PhoneProduct.objects.get(id=id).colors.all().first()
        cart.add(product)
    return redirect(request.META.get('HTTP_REFERER'))


def delete_cart(request, id):
    cart = Cart(request)
    product = ColorCountProduct.objects.get(id=id)
    cart.remove(product)
    return redirect('cart')


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart')


def cart_coupon(request):
    data = datetime.now()
    coupon = request.POST.get('coupon')
    coupon = Coupon.coupon_active.filter(coupon=coupon, start_date__lte=data, end_date__gte=data).first()
    if coupon:
        cart = Cart(request)
        cart.set_coupon(coupon)
        messages.success(request, 'Купон был применен')
    else:
        messages.error(request, 'Купон не действителен')
    return redirect('cart')
