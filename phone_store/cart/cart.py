from django.conf import settings
from store.models import PhoneProduct, LaptopProduct, ColorCountProduct


class Cart(object):
    def __init__(self, request, *args, **kwargs):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID, None)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {'discount':0}
        self.cart = cart


    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        table_name = product._meta.object_name
        memory = product.get_memory_display()
        if table_name not in self.cart:
            self.cart[table_name] = {}
        if product_id not in self.cart[table_name]:
            self.cart[table_name][product_id] = {'id': product_id, 'quantity': 0,
                                                 'price': product.price_discount,
                                                 'color': product.color,
                                                 'memory': memory,
                                                 'name': product.product.name,
                                                 'img': product.product.image.url,
                                                 'prod_slug': product.product.slug,
                                                 }
        self.cart[table_name][product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        table_name = product._meta.object_name
        if product_id in self.cart[table_name]:
            del self.cart[table_name][product_id]
            self.save()

    def set_coupon(self, obj):
        self.cart['discount'] = obj.discount
        self.save()

    def get_total_price(self):
        total_price = 0
        product_name = self.__product_name()
        for prod_name in product_name:
            for item in self.cart[prod_name].values():
                total_price += item['quantity'] * item['price']
        total_price = total_price*(1-self.cart['discount']/100)
        return total_price

    def __iter__(self):
        product_name = self.__product_name()
        for prod_name in product_name:
            for item in self.cart[prod_name]:
                unit = self.cart[prod_name][item]
                unit['total_price'] = int(unit['quantity']) * unit['price']
        for i in product_name:
            for j in self.cart[i].values():
                yield j

    def __len__(self):
        lenght = 0
        product_name = self.__product_name()
        for prod_name in product_name:
            for item in self.cart[prod_name]:
                lenght += int(self.cart[prod_name][item]['quantity'])
        return lenght

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def __product_name(self):
        product_name = self.cart.keys()
        return [i for i in product_name if i != 'discount']
