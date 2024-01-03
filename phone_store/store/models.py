from django.db import models
from django.urls import reverse


# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(active=True)


class Categories(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name


class Manufacture(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя производителя')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='manufactures/', blank=True, null=True)
    slug = models.SlugField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class AbstractProduct(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара')
    slug = models.SlugField(max_length=255, unique=True)
    sale = models.BooleanField(default=False, verbose_name='Скидка')
    discount = models.PositiveIntegerField(default=0, verbose_name='Процент скидки')
    diagonal = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Диоганаль')
    image = models.ImageField(upload_to='store/', blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание')
    original_price = models.PositiveIntegerField(verbose_name='Цена')
    discount_price = models.PositiveIntegerField()
    manufacture = models.ForeignKey(Manufacture, verbose_name='Производитель', on_delete=models.CASCADE)
    frame = models.CharField(max_length=50, verbose_name='Корпус')  # korpus
    height = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Высота')
    width = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ширина')
    thickness = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Толщина')
    weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вес')
    create = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    active = models.BooleanField(default=True)
    new_product = models.BooleanField(default=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.discount_price = self.original_price*(1-self.discount/100)
        return super(AbstractProduct, self).save(*args, **kwargs)


class ColorCountProduct(models.Model):
    ColorChoices = [
        ('BLACK', 'Black'),
        ('WHITE', 'White'),
        ('BLUE', 'Blue'),
        ('BEIGE', 'Beige'),
    ]
    MemoryChoices = [
        ('M_128', '128GB'),
        ('M_256', '256 GB'),
        ('M_512', '512 GB'),
        ('M_1', '1 TB'),
        ('M_2', '2 TB'),

    ]

    color = models.CharField(max_length=100, choices=ColorChoices, verbose_name='Цвет')
    memory = models.CharField(max_length=10, choices=MemoryChoices, verbose_name='Память')
    price = models.PositiveIntegerField(verbose_name='Цена')
    price_discount = models.PositiveIntegerField()
    count = models.PositiveIntegerField(verbose_name='Кол-во')
    product = models.ForeignKey('PhoneProduct', on_delete=models.CASCADE, related_name='colors')

    def save(self, *args, **kwargs):
        self.price_discount = self.price*(1 - self.product.discount/100)
        return super(ColorCountProduct, self).save(*args, **kwargs)

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товаров'


class PhoneProduct(AbstractProduct):
    ConnectorChoices = [
        ('USB', 'USB'),
        ('TPC', 'Type-C'),
        ('LIGHT', 'Lightning'),
        ('MC_USB', 'Micro USB'),
    ]

    BatteryChoices = [
        ('LI', 'Li-Ion'),
        ('NI', 'Ni-Cd'),
        ('NI_MH', 'Ni-MH')
    ]

    display = models.CharField(max_length=20, verbose_name='Дисплей')
    connector = models.CharField(max_length=9, choices=ConnectorChoices, verbose_name='Тип разъема')
    battery_type = models.CharField(max_length=9, choices=BatteryChoices, verbose_name='Тип батареи')

    def __str__(self):
        return self.name

    def save(self):
        return super(PhoneProduct, self).save()

    def get_absolute_url(self):
        return reverse('product_details', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'


class LaptopProduct(AbstractProduct):
    pass
