from rest_framework.views import APIView
from rest_framework.response import Response
from factures.models import FactureService
from factures.models import FactureVente
from clients.models import Client
from .serializers import (
    ClientStatistiquesSerializer,
    FactureVenteStatistiquesSerializer,
    FactureServiceStatistiquesSerializer,
)

class ClientStatistiques(APIView):
    def get(self, request):
        total_clients = Client.objects.count()
        serializer = ClientStatistiquesSerializer({'total_clients': total_clients})
        return Response(serializer.data)

class FactureVenteStatistiques(APIView):
    def get(self, request):
        total_factures = FactureVente.objects.count()
        serializer = FactureVenteStatistiquesSerializer({'total_factures': total_factures})
        return Response(serializer.data)

class FactureServiceStatistiques(APIView):
    def get(self, request):
        total_factures = FactureService.objects.count()
        serializer = FactureServiceStatistiquesSerializer({'total_factures': total_factures})
        return Response(serializer.data)