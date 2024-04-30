
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Commande_ligne
from .serializers import Commande_ligneSerializer  

class CommandeligneView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Commande_ligne.objects.all()
    serializer_class = Commande_ligneSerializer

class CommandeligneCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Commande_ligneSerializer  

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
