# Generated by Django 4.2.11 on 2024-06-05 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_old_image_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='old_image',
        ),
    ]