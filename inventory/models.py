from django.db import models
from django.core.validators import MinValueValidator

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
