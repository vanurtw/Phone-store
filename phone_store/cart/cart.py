from django.conf import settings
from store.models import PhoneProduct, LaptopProduct
from itertools import chain
from decimal import Decimal


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

    def get_total_price(self):
        total_price = 0
        product_name = self.cart.keys()
        for prod_name in product_name:
            for item in self.cart[prod_name].values():
                total_price+=item['quantity']*item['price']
        return total_price

    def __iter__(self):
        product_name = self.cart.keys()
        products_item = []
        for prod_name in product_name:
            if prod_name == 'PhoneProduct':
                products_ids = self.cart[prod_name].keys()
                products = PhoneProduct.objects.filter(id__in=products_ids)
                for product in products:
                    self.cart[prod_name][str(product.id)]['product'] = product
                    self.cart[prod_name][str(product.id)]['price'] = product.original_price
                    quantity = self.cart[prod_name][str(product.id)]['quantity']
                    self.cart[prod_name][str(product.id)]['total_price'] = product.original_price * quantity
        for i in product_name:
            for j in self.cart[i].values():
                yield j

    def __len__(self):
        lenght = 0
        product_name = self.cart.keys()
        for prod_name in product_name:
            for item in self.cart[prod_name]:
                lenght += self.cart[prod_name][item]['quantity']
        return lenght

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
