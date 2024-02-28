import random
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from inventory.models import Item 

class Command(BaseCommand):
    help = 'Create test data for items'

    def handle(self, *args, **kwargs):
        # Clear existing items
        Item.objects.all().delete()

        # Create 40 random items
        for _ in range(40):
            name = get_random_string(length=10)
            description = get_random_string(length=20)
            price = random.uniform(1, 1000)
            quantity = random.randint(1, 100)
            category = random.choice(['Electronics', 'Clothing', 'Books', 'Toys'])

            Item.objects.create(
                name=name,
                description=description,
                price=price,
                quantity=quantity,
                category=category,
            )

        self.stdout.write(self.style.SUCCESS('Successfully created 40 items'))
