from django.db import models


# Create your models here.
class Manufacture(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AbstractProduct(models.Model):
    MemoryChoices = [
        ('M_128', '128GB'),
        ('M_256', '256 GB'),
        ('M_512', '512 GB'),
        ('M_1', '1 TB'),
        ('M_2', '2 TB'),

    ]

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    sale = models.BooleanField(default=False)
    original_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField()
    diagonal = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='media/store/}', blank=True, null=True)
    description = models.TextField()
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE, related_name='manufactures')
    memory = models.CharField(max_length=6, choices=MemoryChoices)
    frame = models.CharField(max_length=50)  # korpus
    height = models.DecimalField(max_digits=10, decimal_places=2)
    width = models.DecimalField(max_digits=10, decimal_places=2)
    Thickness = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True


class ColorCountProduct(models.Model):
    ColorChoices = [
        ('BLACK', 'Black'),
        ('WHITE', 'White'),
        ('BLUE', 'Blue'),
        ('BEIGE', 'Beige'),
    ]

    color = models.CharField(max_length=100, choices=ColorChoices)
    count = models.PositiveIntegerField()
    product = models.ForeignKey('PhoneProduct', on_delete=models.CASCADE, related_name='colors')

    def __str__(self):
        return self.color


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

    display = models.CharField(max_length=20)
    Connector = models.CharField(max_length=9, choices=ConnectorChoices)
    Battery_type = models.CharField(max_length=9, choices=BatteryChoices)

    def __str__(self):
        return self.name
