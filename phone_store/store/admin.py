from django.contrib import admin
from .models import Manufacture, PhoneProduct, ColorCountProduct, Categories, Comments


# Register your models here.

@admin.register(Manufacture)
class ManufactureAdmin(admin.ModelAdmin):
    pass


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
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


@admin.register(ColorCountProduct)
class ColorCountProductAdmin(admin.ModelAdmin):
    pass
