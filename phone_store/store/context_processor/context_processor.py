from cart.cart import Cart
from wishlist.wishlist import Wishlist


def cart_context(request):
    return {'cart': Cart(request)}


def wishlist_context(request):
    return {'wishlist': Wishlist(request)}
