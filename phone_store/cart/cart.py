from django.conf import settings
from store.models import PhoneProduct, LaptopProduct


class Cart(object):
    def __init__(self, request, *args, **kwargs):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID, None)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        table_name = product._meta.object_name
        if table_name not in self.cart:
            self.cart[table_name] = {}
        if product_id not in self.cart[table_name]:
            self.cart[table_name][product_id] = {'quantity': 0, 'price': product.original_price}
        if update_quantity:
            self.cart[table_name][product_id]['quantity'] = quantity
        else:
            self.cart[table_name][product_id]['quantity'] += 1
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        table_name = product._meta.object_name
        if product_id in self.cart[table_name]:
            del self.cart[table_name][product_id]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
