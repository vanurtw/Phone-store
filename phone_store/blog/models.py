from django.db import models


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='Слаг')
    content = models.TextField(verbose_name='Контент')
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='items', verbose_name='Категория')
    image = models.ImageField(upload_to='blog', blank=True, null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
