# Generated by Django 4.2.1 on 2023-05-23 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_restful', '0015_alter_envio_comuna_destino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='comuna_destino',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
