# Generated by Django 2.0.1 on 2018-02-01 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20180129_1203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'permissions': (('customer', 'Customer Rights'),)},
        ),
    ]
