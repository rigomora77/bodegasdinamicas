# Generated by Django 4.1.7 on 2023-02-28 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockrooms', '0016_alter_inventory_store'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='inventory',
            unique_together={('part', 'store')},
        ),
    ]
