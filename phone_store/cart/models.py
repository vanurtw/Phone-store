from django.db import models


# Create your models here.


class Coupon(models.Model):
    coupon = models.CharField(max_length=20, verbose_name='Купон')
    active = models.BooleanField(default=True, verbose_name='Активный')
    start_date = models.DateTimeField(verbose_name='Дата начала')
    end_date = models.DateTimeField(verbose_name='Дата конца')
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.coupon

    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'
