from django.http import HttpResponse
from django.shortcuts import render, redirect

from cart.cart import Cart
from store.models import PhoneProduct, ColorCountProduct


# Create your views here.
def cart(request):
    contex = {'chapter': 'None'}
    cart = Cart(request)
    if cart:
        contex['cart'] = cart
        return render(request, 'cart/cart.html', context=contex)
    return render(request, 'cart/empty-cart.html', context=contex)


def add_cart(request, id, slug):
    cart = Cart(request)
    if request.method == 'POST':
        color = request.GET.get('color')
        memory = request.GET.get('memory')
        quantity = request.POST.get('quantity')
        product = PhoneProduct.objects.get(id=id).colors.get(color=color.upper(), memory=memory)
        cart.add(product, quantity=int(quantity), update_quantity=True)
    else:
        product = PhoneProduct.objects.get(id=id).colors.all().first()
        cart.add(product)
    return redirect('shop')


def delete_cart(request, id):

    cart = Cart(request)
    product = ColorCountProduct.objects.get(id=id)
    cart.remove(product)
    return redirect('cart')


def aaa(request):
    cart = Cart(request)
    cart.clear()
    return HttpResponse('awdwa')
