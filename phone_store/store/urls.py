from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('shop/', views.ShopListView.as_view(), name='shop'),
    path('product-details/<slug:product_slug>/', views.ProductDetailView.as_view(), name='product_details'),
    path('new-letter-sub/', views.new_letter_sub, name='new_sub'),

]
