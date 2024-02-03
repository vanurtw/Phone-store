from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Manufacture, PhoneProduct, ColorCountProduct, Categories, Comments
from .forms import SetQuantityGoods


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
    list_display_links = ['name']
    list_filter = ['create', 'colors__memory', 'colors__color', 'sale', 'new_product']
    list_display = ['id', 'name', 'sale', 'new_product']


@admin.register(ColorCountProduct)
class ColorCountProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'color', 'memory', 'count', 'active']
    list_filter = ['product', 'color', 'memory']
    search_fields = ['product__name', 'color', 'memory']

    actions = ['set_quantity_goods']

    @admin.action(description='Установить колличество товара')
    def set_quantity_goods(self, request, queryset):
        form = None

        if 'count' in request.POST:
            form = SetQuantityGoods(request.POST)
            score = 0
            if form.is_valid():
                count = form.cleaned_data['count']
                for item in queryset:
                    item.count = count
                    item.save()
                    score += 1
                self.message_user(request, f'Для {score} выбранных товаров товаров, установлено колличество {count}')
                return HttpResponseRedirect(request.get_full_path())
        if not form:
            form = SetQuantityGoods(initial={'_selected_action': request.POST.getlist('_selected_action')})
        return render(request, 'admin/set_count.html',
                      {'form': form, 'title': 'Установить колличество', })
