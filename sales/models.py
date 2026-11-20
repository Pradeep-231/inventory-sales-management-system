from django.db import models
from products.models import Product
from django.core.exceptions import ValidationError

# Create your models here.        
class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    sold_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} units"

    def clean(self):
        if self.quantity <= 0:
            raise ValidationError("Quantity must be greater than zero")

        if self.pk is None and self.quantity > self.product.stock_quantity:
            raise ValidationError("Not enough stock available")

    def save(self, *args, **kwargs):
        if self.pk is None:
            if self.quantity <= 0:
                raise ValidationError("Quantity must be greater than zero")

            if self.quantity > self.product.stock_quantity:
                raise ValidationError("Not enough stock available")

            self.product.stock_quantity -= self.quantity
            self.product.save()

        super().save(*args, **kwargs)

