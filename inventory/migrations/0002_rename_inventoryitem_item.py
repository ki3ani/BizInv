# Generated by Django 5.0.2 on 2024-02-28 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InventoryItem',
            new_name='Item',
        ),
    ]
