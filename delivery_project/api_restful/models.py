from django.db import models
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.utils.timezone import datetime
# Create your models here.
# class Paquete(models.Model):
#     title = models.CharField(max_length=255, default='blank title')
#     content = models.CharField(max_length=500, default='blank')
#     content2 = models.CharField(max_length=500, default='blank')


# class Envio(models.Model):
#     ESTADO_CHOICES = (
#         ('PREPARACION', 'En preparación en centro de distribución'),
#         ('TRANSITO', 'En tránsito hacia el destino'),
#         ('ENTREGADO', 'Recepcionado por el destinatario'),
#     )
    
#     numero_seguimiento = models.CharField(max_length=100, unique=True)
#     estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PREPARACION')
#     destinatario = models.CharField(max_length=100)
#     direccion_destino = models.CharField(max_length=200)
#     fecha_entrega = models.DateField(null=True, blank=True)
#     fecha_creacion = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.numero_seguimiento
    

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# class Envio(models.Model):
#     numero_seguimiento = models.CharField(max_length=7, unique=True, editable=False)
#     direccion_origen = models.CharField(max_length=100, default="CD de distribución")
#     nombre_destinatario = models.CharField(max_length=100)
#     direccion_destinatario = models.CharField(max_length=100)
#     fecha_hora_recepcion = models.DateTimeField(null=True, blank=True)
#     fecha_creacion = models.DateTimeField(default=datetime.now, editable=False)
#     sucursal_destino = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
class Envio(models.Model):
    numero_seguimiento = models.CharField(max_length=7, unique=True, editable=False)
    direccion_origen = models.CharField(max_length=100, default="CD de distribución ENEA PUDAHUEL")
    nombre_destinatario = models.CharField(max_length=100)
    direccion_destinatario = models.CharField(max_length=100, blank=True)
    email_destinatario = models.CharField(max_length=100, null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    items_count = models.IntegerField(default=1)
    cellphone = models.CharField(max_length=100, null=True, blank=True)
    destiny = models.CharField(max_length=100, null=True, blank=True)
    address_attributes = models.CharField(max_length=100, blank=True)
    branch_office_id = models.IntegerField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_hora_recepcion = models.DateTimeField(null=True, blank=True)
    sucursal_destino = models.ForeignKey(Sucursal, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.numero_seguimiento

    def save(self, *args, **kwargs):
        if not self.numero_seguimiento:
            self.numero_seguimiento = get_random_string(length=7, allowed_chars='0123456789')
        return super().save(*args, **kwargs)

class EstadoEnvio(models.Model):
    envio = models.ForeignKey(Envio, on_delete=models.CASCADE)
    estado = models.CharField(max_length=100)
    fecha_hora_cambio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.estado