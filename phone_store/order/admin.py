from django.contrib import admin
from .models import Order, OrderItem


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'paid', 'data_create']
    list_filter = ['user', 'paid', 'data_create']
    search_fields = ['user', 'first_name']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass
