# Generated by Django 2.0.1 on 2018-02-02 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturing', '0011_auto_20180202_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wholesalecar',
            name='quantity',
        ),
    ]