# Generated by Django 2.0.1 on 2018-01-25 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturing', '0003_manufactureradmin_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufactureradmin',
            name='manufacturer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manufacturing.Manufacturer'),
        ),
    ]
