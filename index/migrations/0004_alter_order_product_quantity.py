# Generated by Django 5.1.3 on 2024-11-17 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_order_shipping_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_quantity',
            field=models.CharField(max_length=255),
        ),
    ]