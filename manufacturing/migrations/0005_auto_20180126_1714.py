# Generated by Django 2.0.1 on 2018-01-26 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturing', '0004_auto_20180125_1853'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manufactureradmin',
            options={'permissions': (('initiate_manufacturing_order', 'Initiate a Manufacturing Order'), ('crud_blueprint', 'Create/Edit/Delete a Blueprint'), ('modify_cars', 'Modify/Remove Cars from his/her Manufacturer’s Inventory'))},
        ),
        migrations.AddField(
            model_name='wholesalecar',
            name='blueprint',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manufacturing.Blueprint'),
        ),
    ]
