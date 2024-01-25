from django.db import models
from django.contrib.auth.models import User
from store.models import ColorCountProduct


# Create your models here.

class Order(models.Model):
    city_choice = [
        ('MSK', 'Moscow'),
        ('VRN', 'Voronezh'),

    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    price = models.IntegerField(blank=True, verbose_name='Стоимость заказа')
    discount = models.IntegerField(verbose_name='Скидка')
    paid = models.BooleanField(default=False, verbose_name='Заказ оплачен')
    first_name = models.CharField(max_length=50, verbose_name='Имя заказчика')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия заказчика')
    company_name = models.CharField(max_length=80, verbose_name='Имя компании')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    city = models.CharField(max_length=3, choices=city_choice, verbose_name='Город')
    postcode = models.CharField(max_length=20, verbose_name='Почтовый индекс')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Почта')
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    order_notes = models.TextField(blank=True, verbose_name='Комментарии к заказу')

    def __str__(self):
        return f'Order_{self.user}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(ColorCountProduct, on_delete=models.CASCADE, verbose_name='Продукт')
    memory = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField()

    def __str__(self):
        return f'{self.order}_{self.product}'

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.price
        super(OrderItem, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Тип Заказа'
        verbose_name_plural = 'Типы заказов'
