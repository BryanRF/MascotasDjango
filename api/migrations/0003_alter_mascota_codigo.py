# Generated by Django 4.2.6 on 2023-10-21 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_mascota_raza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='codigo',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
