# Generated by Django 2.0.1 on 2018-01-26 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturing', '0005_auto_20180126_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='wholesalecar',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]