from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Client)
admin.site.register(Devis)
admin.site.register(BonDeCommande)
admin.site.register(BonDeLivraison)
admin.site.register(AvoirClient)
admin.site.register(BonDeRetour)