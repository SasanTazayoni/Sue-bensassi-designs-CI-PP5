# Generated by Django 4.2.11 on 2024-06-19 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_fakeitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]
