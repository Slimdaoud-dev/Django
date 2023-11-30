from django.db import models


class Client(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.IntegerField(max_length=8)
    ville = models.TextField()
    soldefacture = models.FloatField(default=0.0)
    soldeglobal = models.FloatField(default=0.0)
    
    # Ajoutez d'autres champs si nécessaire
    def __str__(self):
        return self.nom
    
class Devis(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_devis = models.DateField()
    produits = models.TextField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    # Ajoutez d'autres champs si nécessaire
    def __str__(self):
        return self.client


class BonDeCommande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_commande = models.DateField()
    produits = models.TextField()
    quantites = models.TextField()
    # Ajoutez d'autres champs si nécessaire
    def __str__(self):
        return str(self.produits)


class BonDeLivraison(models.Model):
    commande = models.ForeignKey(BonDeCommande, on_delete=models.CASCADE)
    date_livraison = models.DateField()
    produits_livres = models.TextField()
    quantites_livrees = models.TextField()
    # Ajoutez d'autres champs si nécessaire
    def __str__(self):
        return str(self.commande)


class Facture(models.Model):
    commande = models.ForeignKey(BonDeCommande, on_delete=models.CASCADE)
    date_facture = models.DateField()
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)
    numero_facture = models.CharField(max_length=50)
    statut = models.CharField(max_length=20)
    # Ajoutez d'autres champs si nécessaire
    def __str__(self):
        return str(self.numero_facture)


class AvoirClient(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_avoir = models.DateField()
    montant_avoir = models.DecimalField(max_digits=10, decimal_places=2)
    numero_avoir = models.CharField(max_length=50)
    motif = models.TextField()
    # Ajoutez d'autres champs si nécessaire
    def __str__(self):
        return str(self.numero_avoir)


class BonDeRetour(models.Model):
    commande = models.ForeignKey(BonDeCommande, on_delete=models.CASCADE)
    date_retour = models.DateField()
    produits_retournes = models.TextField()
    quantites_retournees = models.TextField()
    # Ajoutez d'autres champs si nécessaire
    def __str__(self):
        return str(self.produits_retournes)