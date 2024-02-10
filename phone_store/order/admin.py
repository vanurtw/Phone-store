from django.contrib import admin
from .models import Order, OrderItem
import csv


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'paid', 'data_create']
    list_filter = ['user', 'paid', 'data_create']
    search_fields = ['user', 'first_name']
    actions = ['upload_csv']

    @admin.action(description='Сохранить в csv файл')
    def upload_csv(self, request, queryset):
        with open('cart.csv', 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(
                ['Стоимость заказа', 'Скидка', 'Заказ оплачен', 'Имя заказчика', 'Фамилия заказчика', 'Адрес', 'Город',
                 'Телефон', 'Почта', 'Дата создания', 'Комментарии к заказу'])
            for i in queryset.values_list('price', 'discount', 'paid', 'first_name', 'last_name', 'address', 'city',
                                          'phone', 'email', 'data_create', 'order_notes'):
                writer.writerow(i)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass
