# Generated by Django 3.1.5 on 2021-01-27 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
    ]
