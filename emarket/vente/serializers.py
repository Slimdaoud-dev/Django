from rest_framework import serializers
from .models import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model =Client 
        fields = "__all__"
class DevisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devis
        fields = "__all__"
        
class BonDeCommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BonDeCommande
        fields = "__all__"
        
        
class BonDeLivraisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = BonDeLivraison
        fields = "__all__"
        
class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = "__all__"
        
        
class AvoirClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvoirClient
        fields = "__all__"


class BonDeRetourSerializer(serializers.ModelSerializer):
    class Meta:
        model = BonDeRetour
        fields = "__all__"
        