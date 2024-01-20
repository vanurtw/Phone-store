from django.shortcuts import render
from .forms import OrderForm
from cart.cart import Cart


# Create your views here.


def order(request):
    cart = Cart(request)
    form = OrderForm()
    context = {'form': form}
    return render(request, 'order/checkout.html', context)
