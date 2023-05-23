# from rest_framework.viewsets import ModelViewSet
# from api_restful.models import  Paquete, Envio
# from .serializers import EnvioSerializer

# from django.core.mail import send_mail
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import action
# from rest_framework import viewsets

# class PostApiViewSet(ModelViewSet):

#     #serializer_set
#     queryset = Paquete.objects.all()

# #class EnvioViewSet(ModelViewSet):
# #    queryset = Envio.objects.all()
# #    serializer_class = EnvioSerializer

# class EnvioViewSet(viewsets.ModelViewSet):
#     # ...

#     @action(detail=True, methods=['put'])
#     def cambiar_estado(self, request, pk=None):
#         paquete = self.get_object()
#         nuevo_estado = request.data.get('estado')

#         if nuevo_estado:
#             paquete.estado = nuevo_estado
#             paquete.save()

#             # Envío de correo al destinatario
#             send_mail(
#                 'Estado del paquete',
#                 f'El estado de su paquete con número de seguimiento {paquete.numero_seguimiento} ha cambiado a {paquete.get_estado_display()}.',
#                 'noreply@example.com',
#                 [paquete.destinatario],
#                 fail_silently=False,
#             )

#             return Response({'message': 'Estado cambiado correctamente.'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Estado no especificado.'}, status=status.HTTP_400_BAD_REQUEST)
        



from rest_framework import generics, viewsets
from api_restful.models import Envio, EstadoEnvio, Sucursal
from .serializers import EnvioSerializer, EstadoEnvioSerializer, SucursalSerializer

class EnvioListCreateView(generics.ListCreateAPIView):
    queryset = Envio.objects.all()
    serializer_class = EnvioSerializer

class EnvioRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Envio.objects.all()
    serializer_class = EnvioSerializer

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