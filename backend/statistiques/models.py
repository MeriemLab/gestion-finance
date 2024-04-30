from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=100)
    # Ajoutez d'autres champs selon vos besoins

class ServiceFactures(models.Model):
    # Définissez le modèle pour les factures de service
    pass

class VenteFactures(models.Model):
    # Définissez le modèle pour les factures de vente
    pass