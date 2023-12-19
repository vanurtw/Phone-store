from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('shop/', views.shop_page, name='shop'),
    path('product-details/<slug:product_slug>/', views.product_details, name='product_details'),
    path('aaa/', views.aaa)
]
