# Generated by Django 5.0.2 on 2024-02-28 16:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='stock_threshold',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
