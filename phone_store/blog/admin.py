from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Categories, Post, Comment
from .forms import CategorySetPostForm


# Register your models here.


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'data_create', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'data_create']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['category']
    actions = ['set_catery_post']

    @admin.action(description='Установить категорию')
    def set_catery_post(self, request, queryset):
        if 'apply' in request.POST:
            form = CategorySetPostForm(request.POST)
            score = 0
            if form.is_valid():
                category = form.cleaned_data['category']
                for item in queryset:
                    score += 1
                    item.category=category
                    item.save()
                self.message_user(request, f'Для {score} выбранных постов, установлена категория {category}')
                return HttpResponseRedirect(request.get_full_path())
        else:
            form = CategorySetPostForm(initial={'_selected_action': request.POST.getlist('_selected_action')})
        return render(request, 'admin_set_category.html',
                      {'items': queryset, 'form': form, 'title': 'Установить категорию'})


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'data_create']
    list_filter = ['user', 'post__title', 'data_create']
