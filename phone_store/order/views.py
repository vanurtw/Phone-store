from django.shortcuts import render
from .forms import OrderForm
from cart.cart import Cart


# Create your views here.


def order_user(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
    else:
        form = OrderForm()
    context = {'form': form}
    return render(request, 'order/checkout.html', context)
