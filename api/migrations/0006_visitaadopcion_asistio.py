# Generated by Django 4.2.6 on 2023-10-22 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_visitaadopcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitaadopcion',
            name='asistio',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
