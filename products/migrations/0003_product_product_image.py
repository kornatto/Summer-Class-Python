# Generated by Django 5.2.3 on 2025-07-22 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_stock_alter_product_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/products/'),
        ),
    ]
