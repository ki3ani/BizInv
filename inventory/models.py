from django.core.mail import send_mail
from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings

class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    stock_threshold = models.IntegerField(default=10, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Call the real save method first to ensure the item is saved in the database
        super(Item, self).save(*args, **kwargs)
        
        # After saving, check if the stock level is at or below the threshold
        if self.quantity <= self.stock_threshold:
            # If so, construct and send an email alert
            subject = f'Stock Alert for {self.name}'
            message = f'The stock for "{self.name}" is below the threshold. Current stock: {self.quantity}.'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['kimanim68@gmail.com']  # Replace with actual recipient email address
            
            # Send the email alert
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
