from django.urls import path
from . import views
urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('cart-add/<int:id>/<slug:slug>/', views.add_cart, name='cart_add'),
    path('cart-delete/<int:id>/', views.delete_cart, name='cart_delete'),
    path('aaa/', views.aaa)
]
