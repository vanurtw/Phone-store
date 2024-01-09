from django.shortcuts import render, redirect
from .wishlist import Wishlist
from store.models import ColorCountProduct, PhoneProduct
from django.http import HttpResponse
from cart.cart import Cart


# Create your views here.


def wishlist(request):
    context = {}
    wishlist = Wishlist(request)
    context['wishlist'] = wishlist
    return render(request, 'wishlist/wishlist.html', context)


def add_wishlist(request, id):
    wishlist = Wishlist(request)
    if not request.GET.get('wis'):
        obj = PhoneProduct.objects.get(id=id).colors.all().first()
        id = obj.id
    wishlist.add(id)
    return redirect(request.META.get('HTTP_REFERER'))


def delete(request, id):
    wishlist = Wishlist(request)
    wishlist.delete(id)
    return redirect('wishlist')


def cart_add_wishlist(request, id):
    cart = Cart(request)
    wishlist = Wishlist(request)
    product = ColorCountProduct.objects.get(id=id)
    cart.add(product)
    wishlist.delete(str(id))
    return redirect('wishlist')
