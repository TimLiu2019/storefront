# Generated by Django 3.2.6 on 2021-08-11 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
    ]
