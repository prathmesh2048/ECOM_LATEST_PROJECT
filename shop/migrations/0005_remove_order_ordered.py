# Generated by Django 3.1.5 on 2021-01-28 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered',
        ),
    ]