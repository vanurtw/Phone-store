from django.contrib import admin
from .models import Categories, Post


# Register your models here.


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'data_create']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['']
