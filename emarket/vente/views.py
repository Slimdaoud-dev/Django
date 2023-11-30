from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework import status

@api_view(['GET'])

def get_all_clients(request):
   clients = Client.objects.all()
   serializer = ClientSerializer(clients,many=True)
   
   return Response ({"Clients" :serializer.data})


@api_view(['GET'])

def get_all_clients_by_id(request,pk):
   client = get_object_or_404(Client,id=pk)
   serializer = ClientSerializer(client,many=False)
   
   return Response ({"client" :serializer.data})

@api_view(['POST'])

def newclient(request):
   data = request.data
   serializer = ClientSerializer(data = data)
   if serializer.is_valid():
      client = Client.objects.create(**data)
      res = ClientSerializer(client,many=False)
   
   
   return Response ({"client" :res.data})


@api_view(['DELETE'])

def delete_client(request,pk):
   client = get_object_or_404(Client,id=pk)
   client.delete()
   return Response ({"details":"delete is done" },status=status.HTTP_200_OK)

@api_view(['GET'])

def get_all_devis(request):
   devis = Devis.objects.all()
   serializer = DevisSerializer(devis,many=True)
   
   return Response ({"Devis" :serializer.data})


@api_view(['GET'])

def get_all_devis_by_id(request,pk):
   devi = get_object_or_404(Devis,id=pk)
   serializer = DevisSerializer(devi,many=False)
   
   return Response ({"devi" :serializer.data})

@api_view(['GET'])

def get_all_Facture(request):
   factures = Facture.objects.all()
   serializer = FactureSerializer(factures,many=True)
   
   return Response ({"Factures" :serializer.data})


@api_view(['GET'])

def get_all_factures_by_id(request,pk):
   facture = get_object_or_404(Facture,id=pk)
   serializer = FactureSerializer(facture,many=False)
   
   return Response ({"facture" :serializer.data})

@api_view(['GET'])

def get_all_BonDeCommande(request):
   BonDeCommandes = BonDeCommande.objects.all()
   serializer = BonDeCommandeSerializer(BonDeCommandes,many=True)
   
   return Response ({"Bon de Commandes" :serializer.data})

@api_view(['GET'])

def get_all_commande_by_id(request,pk):
   commande = get_object_or_404(BonDeCommande,id=pk)
   serializer = BonDeCommandeSerializer(commande,many=False)
   
   return Response ({"bon de commande" :serializer.data})

@api_view(['GET'])

def get_all_BonDeLivraison(request):
   BonDeLivraisons = BonDeLivraison.objects.all()
   serializer = BonDeLivraisonSerializer(BonDeLivraisons,many=True)
   
   return Response ({"Bon de livraisons" :serializer.data})

@api_view(['GET'])

def get_all_livraison_by_id(request,pk):
   livraison = get_object_or_404(BonDeLivraison,id=pk)
   serializer = BonDeLivraisonSerializer(livraison,many=False)
   
   return Response ({"BonDeLivraison" :serializer.data})

@api_view(['GET'])

def get_all_AvoirClient(request):
   AvoirClients = AvoirClient.objects.all()
   serializer = AvoirClientSerializer(AvoirClients,many=True)
   
   return Response ({"Avoirs" :serializer.data})

@api_view(['GET'])

def get_all_avoir_by_id(request,pk):
   avoir = get_object_or_404(AvoirClient,id=pk)
   serializer = AvoirClientSerializer(avoir,many=False)
   
   return Response ({"avoir" :serializer.data})

@api_view(['GET'])

def get_all_BonDeRetour(request):
   BonDeRetours = BonDeRetour.objects.all()
   serializer = BonDeRetourSerializer(BonDeRetours,many=True)
   
   return Response ({"Bon de retours" :serializer.data})

@api_view(['GET'])

def get_all_retour_by_id(request,pk):
   retour = get_object_or_404(BonDeRetour,id=pk)
   serializer = BonDeCommandeSerializer(retour,many=False)
   
   return Response ({"bon de retour" :serializer.data})