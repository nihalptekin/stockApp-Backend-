# Generated by Django 4.2.4 on 2023-09-27 11:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_remove_category_products_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchases',
            name='price_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]