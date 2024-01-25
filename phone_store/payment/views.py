from django.shortcuts import render, redirect, get_object_or_404, reverse
import stripe
from order.models import Order
from django.conf import settings
import decimal

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


def process_payment(request):
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        success_url = request.build_absolute_uri(reverse('completed'))
        cancel_url = request.build_absolute_uri(reverse('cancel'))
        session_data = {
            'mode': 'payment',
            'client_reference_id': order.id,
            'success_url': success_url,
            'cancel_url': cancel_url,
            'line_items': []
        }
        for item in order.items.all():
            success_url['line_items'].append({
                'price_data': {
                    'unit_amount': int(item.total_price * decimal.Decimal('100')), 'currency': 'RUB',
                    'product_data': {
                        'name': item.product.product.name,
                    },
                },
                'quantity': item.quantity,

            })

        session = stripe.checkout.Session.create(**session_data)
        return redirect(session.url, code=303)
    return render(request, 'payment/process.html', locals())


def payment_completed(request):
    return render(request, 'payment/completed.html')


def payment_cancel(request):
    return render(request, 'payment/cancel.html')
