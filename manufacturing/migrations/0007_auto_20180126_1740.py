# Generated by Django 2.0.1 on 2018-01-26 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturing', '0006_wholesalecar_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wholesalecar',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
