# Generated by Django 2.0.1 on 2018-01-29 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wholesaledeal',
            name='car_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacturing.WholesaleCar'),
        ),
    ]