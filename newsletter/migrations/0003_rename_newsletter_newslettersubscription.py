# Generated by Django 4.2.11 on 2024-06-18 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_alter_newsletter_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Newsletter',
            new_name='NewsletterSubscription',
        ),
    ]
