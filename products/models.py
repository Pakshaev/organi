from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']
        verbose_name = 'отдел'
        verbose_name_plural = 'Отделы'  

    def __str__(self):
        return self.name

class Colors(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']
        verbose_name = 'цвет'
        verbose_name_plural = 'Цвета'  

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    color = models.ForeignKey(Colors, on_delete=models.CASCADE)
    size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    description_short = models.TextField()
    description_long = models.TextField()
    availability = models.BooleanField(default=True)
    weight = models.FloatField()
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'продукт'
        verbose_name_plural = 'Продукты'    

    def __str__(self):
        return self.name
    
    def discounted_price(self):
        return self.price * (1 - self.discount / 100)
