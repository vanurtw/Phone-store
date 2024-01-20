from django.db import models


# Create your models here.

class Order(models.Model):
    city_choice = [
        ('MSK', 'Moscow'),
        ('VRN', 'Voronezh'),

    ]
    first_name = models.CharField(max_length=50, verbose_name='Имя заказчика')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия заказчика')
    company_name = models.CharField(max_length=80, verbose_name='Имя компании')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    city = models.CharField(max_length=3, choices=city_choice, verbose_name='Город')
    postcode = models.CharField(max_length=20, verbose_name='Почтовый индекс')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Почта')
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    order_notes = models.TextField(blank=True)

    def __str__(self):
        return f'Order_{self.id}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
