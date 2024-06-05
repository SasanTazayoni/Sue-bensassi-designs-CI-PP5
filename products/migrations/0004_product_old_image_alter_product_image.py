# Generated by Django 4.2.11 on 2024-06-05 15:01

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='old_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]