# Generated by Django 4.1.7 on 2023-02-22 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockrooms', '0002_rename_stores_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='id',
        ),
        migrations.AlterField(
            model_name='store',
            name='code',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Código SAP'),
        ),
    ]