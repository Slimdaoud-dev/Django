from django.urls import path

from . import views


urlpatterns = [
    path("clients/", views.get_all_clients),
    path("clients/<str:pk>", views.get_all_clients_by_id),
    path("clients/delete/<str:pk>", views.delete_client),
    path("clients/new/", views.newclient),
    path("devis/", views.get_all_devis),
    path("devis/<str:pk>", views.get_all_devis_by_id), 
    path("Facture/", views.get_all_Facture),
    path("Facture/<str:pk>", views.get_all_factures_by_id), 
    path("BonDeCommande/", views.get_all_BonDeCommande),
    path("BonDeCommande/<str:pk>", views.get_all_commande_by_id), 
    path("BonDeLivraison/", views.get_all_BonDeLivraison),
    path("BonDeLivraison/<str:pk>", views.get_all_livraison_by_id), 
    path("BonDeRetour/", views.get_all_BonDeRetour),
    path("BonDeRetour/<str:pk>", views.get_all_retour_by_id), 
    path("AvoirClient/", views.get_all_AvoirClient),
    path("AvoirClient/<str:pk>", views.get_all_avoir_by_id),
   
]
