from django.db import models
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.utils.timezone import datetime
# Create your models here.

    
class Sucursal(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Envio(models.Model):
    numero_seguimiento = models.CharField(max_length=7, unique=True, editable=False)
    direccion_origen = models.CharField(max_length=100, default="CD de distribución ENEA PUDAHUEL")
    nombre_destinatario = models.CharField(max_length=100)
    comuna_destino = models.CharField(max_length=100, blank=True)
    direccion_destinatario = models.CharField(max_length=100, blank=True)
    email_destinatario = models.CharField(max_length=100, null=True, blank=True)
    height = models.FloatField( default=1)
    width = models.FloatField(default=1)
    length = models.FloatField( default=1)
    weight = models.FloatField( default=1)
    items_count = models.IntegerField(default=1)
    cellphone = models.CharField(max_length=100, null=True, blank=True)
    destiny = models.CharField(max_length=100, null=True, blank=True)
    address_attributes = models.CharField(max_length=100, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_hora_recepcion = models.DateTimeField(null=True, blank=True)
    sucursal_destino = models.ForeignKey(Sucursal, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.numero_seguimiento

    def save(self, *args, **kwargs):
        if not self.numero_seguimiento:
            self.numero_seguimiento = get_random_string(length=7, allowed_chars='0123456789')
        return super().save(*args, **kwargs)
    


# class EstadoEnvio(models.Model):
#     envio = models.ForeignKey(Envio, on_delete=models.CASCADE)
#     estado = models.CharField(max_length=100)
#     fecha_hora_cambio = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.estado
    


class EstadoEnvio(models.Model):
    ESTADOS_CHOICES = [
        ('EN_PREPARACION', 'En preparación'),
        ('EN_RUTA_A_DESTINO', 'En ruta a destino'),
        ('ENTREGADO_A_DESTINATARIO', 'Entregado a destinatario'),
        ('CANCELADO', 'Cancelado'),
    ]

    envio = models.ForeignKey(Envio, on_delete=models.CASCADE, related_name='estados')
    estado = models.CharField(max_length=100, choices=ESTADOS_CHOICES)
    fecha_hora_cambio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.estado