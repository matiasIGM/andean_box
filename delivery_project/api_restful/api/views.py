
from rest_framework import generics, viewsets
from api_restful.models import Envio, EstadoEnvio, Sucursal
from .serializers import EnvioSerializer, EstadoEnvioSerializer, SucursalSerializer
from django.shortcuts import get_object_or_404

class EnvioListCreateView(generics.ListCreateAPIView):
    queryset = Envio.objects.all()
    serializer_class = EnvioSerializer

class EnvioRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Envio.objects.all()
    serializer_class = EnvioSerializer

    def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {self.lookup_field: self.kwargs['pk']}
        return get_object_or_404(queryset, numero_seguimiento=filter_kwargs['pk'])


class EstadoEnvioListCreateView(generics.ListCreateAPIView):
    queryset = EstadoEnvio.objects.all()
    serializer_class = EstadoEnvioSerializer

class EstadoEnvioRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EstadoEnvio.objects.all()
    serializer_class = EstadoEnvioSerializer

class SucursalListCreateView(generics.ListCreateAPIView):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

class SucursalRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer