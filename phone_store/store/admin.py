from django.contrib import admin
from .models import Manufacture, PhoneProduct, ColorCountProduct, Categories, Comments


# Register your models here.

@admin.register(Manufacture)
class ManufactureAdmin(admin.ModelAdmin):
    list_display = ['name', 'create']


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rating', 'data_create']


class ColorCountProductInline(admin.StackedInline):
    model = ColorCountProduct
    extra = 2


@admin.register(PhoneProduct)
class PhoneProductAdmin(admin.ModelAdmin):
    inlines = [ColorCountProductInline]
    exclude = ['create']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    list_filter = ['create', 'colors__memory', 'colors__color', 'sale', 'new_product']
    list_display = ['id', 'name', 'sale', 'new_product']


@admin.register(ColorCountProduct)
class ColorCountProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'color', 'memory', 'count', 'active']
    list_filter = ['product', 'color', 'memory']
