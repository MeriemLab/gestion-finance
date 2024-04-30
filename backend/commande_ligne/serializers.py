from rest_framework import serializers
from .models import Commande_ligne

class Commande_ligneSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Commande_ligne
        fields = '__all__'

    def create(self, validated_data):
        return Commande_ligne.objects.create(**validated_data)
