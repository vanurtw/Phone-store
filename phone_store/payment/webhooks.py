from django.conf import settings
from order.models import Order
from django.http import HttpResponse
import stripe
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def webhooks_stripe(request):
    paylod = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(paylod, sig_header, settings.STRIPE_WEBHOOK_SECRET)
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event.type == 'checkout.session.completed':
        session = event.data.object
        if session.mode == 'payment' and session.payment_status == 'paid':
            try:
                order = Order.objects.get(id=session.client_reference_id)
            except Order.DoesNotExist:
                return HttpResponse(status=404)
            # пометить заказ как оплаченный
            order.paid = True
            order.save()
    return HttpResponse(status=200)
