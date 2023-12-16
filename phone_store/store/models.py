from django.db import models


# Create your models here.
class Manufacture(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя производителя')
    slug = models.SlugField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class AbstractProduct(models.Model):

    name = models.CharField(max_length=255, verbose_name='Название товара')
    slug = models.SlugField(max_length=255)
    sale = models.BooleanField(default=False, verbose_name='Скидка')
    discount = models.PositiveIntegerField(default=0, verbose_name='Процент скидки')
    diagonal = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Диоганаль')
    image = models.ImageField(upload_to='store/', blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание')
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE, related_name='manufactures',
                                    verbose_name='Производитель')
    frame = models.CharField(max_length=50, verbose_name='Корпус')  # korpus
    height = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Высота')
    width = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ширина')
    thickness = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Толщина')
    weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вес')
    create = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        abstract = True


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
    count = models.PositiveIntegerField(verbose_name='Кол-во')
    product = models.ForeignKey('PhoneProduct', on_delete=models.CASCADE, related_name='colors')

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
    Connector = models.CharField(max_length=9, choices=ConnectorChoices, verbose_name='Тип разъема')
    Battery_type = models.CharField(max_length=9, choices=BatteryChoices, verbose_name='Тип батареи')

    def __str__(self):
        return self.name

    def save(self):
        return super(PhoneProduct, self).save()

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
