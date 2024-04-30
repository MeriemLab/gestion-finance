from rest_framework import serializers

class ClientStatistiquesSerializer(serializers.Serializer):
    total_clients = serializers.IntegerField()

class FactureVenteStatistiquesSerializer(serializers.Serializer):
    total_factures = serializers.IntegerField()

class FactureServiceStatistiquesSerializer(serializers.Serializer):
    total_factures = serializers.IntegerField()