from django.contrib import admin
from .models import Coupon


# Register your models here.

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['coupon', 'start_date', 'end_date', 'active']
    list_filter = ['active']
    actions = ['not_active_coupon', 'active_coupon']

    @admin.action(description='Сделать не активным')
    def not_active_coupon(self, request, queryset):
        queryset.update(active=False)

    @admin.action(description='Сделать активным')
    def active_coupon(self, request, queryset):
        queryset.update(active=True)
