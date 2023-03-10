# Generated by Django 4.1.7 on 2023-02-27 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockrooms', '0011_alter_inventory_part_alter_inventory_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='part',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stockrooms.part'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='store',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stockrooms.store'),
        ),
    ]
