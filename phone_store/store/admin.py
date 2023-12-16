from django.contrib import admin
from .models import Manufacture, PhoneProduct, ColorCountProduct


# Register your models here.

@admin.register(Manufacture)
class ManufactureAdmin(admin.ModelAdmin):
    pass


class ColorCountProductInline(admin.StackedInline):
    model = ColorCountProduct
    extra = 2


@admin.register(PhoneProduct)
class PhoneProductAdmin(admin.ModelAdmin):
    inlines = [ColorCountProductInline]
    exclude = ['create']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    list_filter = ['create', 'colors__memory', 'colors__color']
