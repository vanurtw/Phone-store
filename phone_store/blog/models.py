from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse
from taggit.managers import TaggableManager


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, blank=True, null=True)
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок', unique=True)
    slug = models.SlugField(max_length=255, verbose_name='Слаг', unique=True)
    content = models.TextField(verbose_name='Контент')
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='items', verbose_name='Категория')
    image = models.ImageField(upload_to='blog', blank=True, null=True, verbose_name='Изображение')
    popular = models.BooleanField(default=False, verbose_name='Популярный пост')
    tags = TaggableManager(verbose_name='Тэги')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_details', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    data_create = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='parent_comments')

    def __str__(self):
        return f'comment_{self.post.id}_{self.user}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
