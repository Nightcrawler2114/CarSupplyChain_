# Generated by Django 2.0.1 on 2018-02-02 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealership', '0011_remove_retailcar_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wholesaledeal',
            name='car_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]