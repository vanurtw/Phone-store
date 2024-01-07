from django.shortcuts import render, redirect
from .wishlist import Wishlist
from store.models import ColorCountProduct, PhoneProduct
from django.http import HttpResponse


# Create your views here.


def wishlist(request):
    context = {}
    wishlist = Wishlist(request)
    context['wishlist'] = wishlist
    return render(request, 'wishlist/wishlist.html', context)


def add_wishlist(request, id):
    wishlist = Wishlist(request)
    if request.method == 'GET':
        obj = PhoneProduct.objects.get(id=id).colors.all().first()
        id = obj.id
    else:
        color = request.GET.get('color')
        memory = request.GET.get('memory')
        obj = PhoneProduct.objects.get(id=id).colors.get(color=color.upper(), memory=memory)
        id = obj.id
    wishlist.add(id)
    return redirect(request.META.get('HTTP_REFERER'))


def clear_wishlist(request):
    wishlist = Wishlist(request)
    wishlist.clear()
    return redirect('wishlist')
