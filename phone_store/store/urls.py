from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('shop/', views.ShopListView.as_view(), name='shop'),
    path('product-details/<slug:product_slug>/', views.product_details, name='product_details'),

]
