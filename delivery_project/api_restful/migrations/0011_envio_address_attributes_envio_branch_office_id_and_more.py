# Generated by Django 4.2.1 on 2023-05-23 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_restful', '0010_envio_fecha_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='envio',
            name='address_attributes',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='envio',
            name='branch_office_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='envio',
            name='cellphone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='envio',
            name='destiny',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='envio',
            name='email_destinatario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='envio',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='envio',
            name='items_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='envio',
            name='length',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='envio',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='envio',
            name='width',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='envio',
            name='direccion_destinatario',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='envio',
            name='direccion_origen',
            field=models.CharField(default='CD de distribución ENEA PUDAHUEL', max_length=100),
        ),
        migrations.AlterField(
            model_name='envio',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='envio',
            name='sucursal_destino',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_restful.sucursal'),
        ),
    ]
