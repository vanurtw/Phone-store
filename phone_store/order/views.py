from django.shortcuts import render
from .forms import OrderForm
from cart.cart import Cart
from .models import OrderItem
from store.models import ColorCountProduct
from django.db.models import F


# Create your views here.


def order_user(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                product = ColorCountProduct.objects.get(id=item['id'])
                quantity = item['quantity']
                product.count = F('count') - quantity
                product.save()
                product.refresh_from_db()
                if product.count <= 0:
                    product.count = 0
                    product.active = False
                    product.save()
                OrderItem.objects.create(order=order, product=product, memory=item['memory'], price=item['price'],
                                         color=item['color'], quantity=quantity)
            cart.clear()

    else:
        form = OrderForm()
        for item in cart:
            product = ColorCountProduct.objects.get(id=item['id'])
            quantity = int(item['quantity'])
            if quantity > product.count:
                item['quantity'] = product.count

    context = {'form': form}
    return render(request, 'order/checkout.html', context)
