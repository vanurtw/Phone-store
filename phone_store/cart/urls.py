from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('cart-add/<int:id>/<slug:slug>/', views.add_cart, name='cart_add'),
    path('cart-delete/<int:id>/', views.delete_cart, name='cart_delete'),
    path('cart-clear/', views.cart_clear, name='cart_clear'),
    path('cart-coupon/', views.cart_coupon, name='cart_coupon'),

]
