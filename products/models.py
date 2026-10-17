from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    minimum_quantity = models.PositiveIntegerField()
    supplier_lead_time = models.PositiveIntegerField()

    def __str__(self):
        return self.name
