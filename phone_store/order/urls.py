from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_user, name='order'),

]
