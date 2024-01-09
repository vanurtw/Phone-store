from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('wishlist-add/<str:id>/', views.add_wishlist, name='add_wishlist'),
    path('wishlist-delete/<str:id>/', views.delete, name='del_wishlist'),

]
