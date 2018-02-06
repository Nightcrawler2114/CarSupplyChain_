# Generated by Django 2.0.1 on 2018-02-06 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturing', '0012_remove_wholesalecar_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wholesalecar',
            name='blueprint',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manufacturing.Blueprint'),
        ),
        migrations.AlterField(
            model_name='wholesalecar',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manufacturing.Manufacturer'),
        ),
    ]
