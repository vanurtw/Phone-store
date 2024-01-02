from django.shortcuts import render, redirect
from .models import PhoneProduct
from cart.cart import Cart
from django.http import HttpResponse


# Create your views here.


def home_page(request):
    products = PhoneProduct.published.all()[:4]
    return render(request, 'store/home.html', {'products': products})


def shop_page(request):
    context = {'chapter': 'shop'}
    context['type_product'] = request.GET.get('type-product', None)
    if context['type_product'] == 'laptop':
        products = []
    elif context['type_product'] == 'iphone':
        products = PhoneProduct.published.all()
    else:
        products = PhoneProduct.published.all()
    context['products'] = products
    return render(request, 'store/shop.html', context)


def product_details(request, product_slug):
    product = PhoneProduct.published.get(slug=product_slug)
    color_product = product.colors.all()
    col = request.GET.get('color', color_product[0].color)
    memory_product = color_product.filter(color__icontains=col)
    memory = request.GET.get('memory', memory_product[0].memory)
    prod = memory_product.get(memory=memory)
    related_products = PhoneProduct.objects.all().order_by('?')[:4]
    context = {'color': col.lower(), 'memory': memory, 'product': product, 'color_product': color_product,
               'chapter': 'shop', 'prod': prod, 'memory_product': memory_product, 'related_products': related_products}
    return render(request, 'store/product-details.html', context=context)
