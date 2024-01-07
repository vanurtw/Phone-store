from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('wishlist-add/<str:id>/', views.add_wishlist, name='add_wishlist'),
    path('wishlist-clear/', views.clear_wishlist, name='clear_wishlist'),

]
