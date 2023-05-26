# from rest_framework.serializers import ModelSerializer
# from api_restful.models import Paquete, Envio

from rest_framework import serializers
from api_restful.models import Envio, EstadoEnvio, Sucursal

# class PostApiViewSet(ModelSerializer):
#     class Meta:
#         Model = Paquete
#         fields =['id', 'title', 'content']

# class EnvioSerializer(ModelSerializer):
#     class Meta:
#         model = Envio
#         fields = '__all__'
#         read_only_fields = ('estado',)  # El estado solo se debe actualizar mediante la acción cambiar_estado


# class EstadoEnvioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EstadoEnvio
#         fields = '__all__'

class EstadoEnvioSerializer(serializers.ModelSerializer):
    estado = serializers.ChoiceField(choices=EstadoEnvio.ESTADOS_CHOICES)

    class Meta:
        model = EstadoEnvio
        fields = '__all__'

# class EnvioSerializer(serializers.ModelSerializer):
#     estados = EstadoEnvioSerializer(many=True, read_only=True)

#     class Meta:
#         model = Envio
#         fields = '__all__'
class EnvioSerializer(serializers.ModelSerializer):
    estados = EstadoEnvioSerializer(many=True, read_only=True)
    estado_actual = serializers.SerializerMethodField()

    class Meta:
        model = Envio
        fields = ['id', 'estados', 'numero_seguimiento', 'direccion_origen', 'nombre_destinatario', 'comuna_destino', 'direccion_destinatario', 'email_destinatario', 'height', 'width', 'length', 'weight', 'items_count', 'cellphone', 'destiny', 'address_attributes', 'fecha_creacion', 'fecha_hora_recepcion', 'sucursal_destino', 'estado_actual']

    def get_estado_actual(self, obj):
        estado_actual = obj.estados.last()
        if estado_actual:
            return estado_actual.estado
        return None

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'







