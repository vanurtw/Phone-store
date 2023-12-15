from django.contrib import admin
from .models import Manufacture, PhoneProduct


# Register your models here.

@admin.register(Manufacture)
class ManufactureAdmin(admin.ModelAdmin):
    pass


@admin.register(PhoneProduct)
class PhoneProductAdmin(admin.ModelAdmin):
    pass
