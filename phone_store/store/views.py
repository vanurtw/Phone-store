from django.shortcuts import render, redirect
from .models import PhoneProduct
from django.views.generic import ListView, DetailView
from .forms import CommentForm, NewsletterSubForm
from django.contrib import messages
import csv


# Create your views here.

class HomeListView(ListView):
    template_name = 'store/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        return PhoneProduct.published.all()[:4]


class ShopListView(ListView):
    template_name = 'store/shop.html'
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShopListView, self).get_context_data(**kwargs)
        context['chapter'] = 'shop'
        context['type_product'] = self.request.GET.get('type-product', None)
        return context

    def get_queryset(self):
        if self.request.GET.get('type-product') == 'laptop':
            return []
        # self.kwargs.get('type_product') == 'iphone':
        return PhoneProduct.published.all()


# na zamenu
class ProductDetailView(DetailView):
    template_name = 'store/product-details.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
    model = PhoneProduct

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        form = form.save(commit=False)
        form.user = request.user
        product_slug = kwargs['product_slug']
        product = PhoneProduct.objects.get(slug=product_slug)
        form.product = product
        form.save()
        return redirect(request.META['HTTP_REFERER'])

    def get_queryset(self):
        slug = self.kwargs['product_slug']
        return PhoneProduct.published.filter(slug=slug)

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        request = self.request
        product = context['product']
        context['form'] = CommentForm()
        color_product = product.colors.all()
        context['color_product'] = color_product
        col = request.GET.get('color', color_product[0].color)
        context['color'] = col.lower()
        context['prod_header'] = request.GET.get('prod-header', 'description')
        memory_product = color_product.filter(color__icontains=col)
        context['memory_product'] = memory_product
        memory = request.GET.get('memory', memory_product[0].memory)
        context['memory'] = memory
        context['chapter'] = 'shop'
        prod = memory_product.get(memory=memory)
        context['prod'] = prod
        related_products = PhoneProduct.objects.all().order_by('?')[:4]
        context['related_products'] = related_products
        return context


def product_details(request, product_slug):
    product = PhoneProduct.published.get(slug=product_slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form = form.save(commit=False)
        form.user = request.user
        form.product = product
        form.save()
        return redirect(request.META['HTTP_REFERER'])
    form = CommentForm()
    color_product = product.colors.all()
    col = request.GET.get('color', color_product[0].color)
    memory_product = color_product.filter(color__icontains=col)
    memory = request.GET.get('memory', memory_product[0].memory)
    prod_header = request.GET.get('prod-header', 'description')
    prod = memory_product.get(memory=memory)
    related_products = PhoneProduct.objects.all().order_by('?')[:4]
    context = {'prod_header': prod_header, 'color': col.lower(), 'memory': memory, 'product': product,
               'color_product': color_product, 'form': form,
               'chapter': 'shop', 'prod': prod, 'memory_product': memory_product, 'related_products': related_products}
    return render(request, 'store/product-details.html', context=context)


def new_letter_sub(request):
    if request.method == 'POST':
        form = NewsletterSubForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы подписались на нашу рыссылку')
        else:
            messages.error(request, 'Ошибка, такая почта уже есть')
    return redirect(request.META['HTTP_REFERER'])
