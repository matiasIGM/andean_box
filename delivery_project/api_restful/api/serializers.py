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


class EstadoEnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoEnvio
        fields = '__all__'

class EnvioSerializer(serializers.ModelSerializer):
    estados = EstadoEnvioSerializer(many=True, read_only=True)

    class Meta:
        model = Envio
        fields = '__all__'

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'