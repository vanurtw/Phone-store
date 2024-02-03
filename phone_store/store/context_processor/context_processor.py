from cart.cart import Cart
from wishlist.wishlist import Wishlist
from store.forms import NewsletterSubForm


def cart_context(request):
    return {'cart': Cart(request)}


def wishlist_context(request):
    return {'wishlist': Wishlist(request)}


def form_sub_context(request):
    return {'form_sub': NewsletterSubForm()}
