from django.db import models
from django.core.validators import MinValueValidator

class Item(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    description = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.name
