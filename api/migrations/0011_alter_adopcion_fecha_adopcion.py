# Generated by Django 4.2.6 on 2023-10-26 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_eventoparticipante_ticket_alter_evento_recaudacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adopcion',
            name='fecha_adopcion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
