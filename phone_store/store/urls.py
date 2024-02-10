from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60* 5)(views.HomeListView.as_view()), name='home'),
    path('shop/', cache_page(60 * 5)(views.ShopListView.as_view()), name='shop'),
    path('product-details/<slug:product_slug>/', views.ProductDetailView.as_view(), name='product_details'),
    path('new-letter-sub/', views.NewLetterSub.as_view(), name='new_sub'),

]
