from django.db import models


# Create your models here.
class ActiveCoupon(models.Manager):
    def get_queryset(self):
        return super(ActiveCoupon, self).get_queryset().filter(active=True)


class Coupon(models.Model):
    coupon = models.CharField(max_length=20, verbose_name='Купон')
    discount = models.PositiveIntegerField(verbose_name='Скидка(%)')
    active = models.BooleanField(default=True, verbose_name='Активный')
    start_date = models.DateTimeField(verbose_name='Дата начала')
    end_date = models.DateTimeField(verbose_name='Дата конца')
    create = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    coupon_active = ActiveCoupon()

    def __str__(self):
        return self.coupon

    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'
