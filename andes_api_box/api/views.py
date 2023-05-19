from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    paquete = {'tipo':'encomienda', 'peso': 100}
    return Response(paquete)