from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('wishlist-add/<str:id>/', views.add_wishlist, name='add_wishlist'),
    path('wishlist-delete/<str:id>/', views.delete, name='del_wishlist'),
    path('wishlist_cart_add/<int:id>/', views.cart_add_wishlist, name='wishlist_add_cart'),


]
