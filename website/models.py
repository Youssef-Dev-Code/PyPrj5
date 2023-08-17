from typing import Any
from django.db import models

class Banque(models.Model):
    Designation = models.CharField(max_length=50)

class Local(models.Model):
    Designation = models.CharField(max_length=25)

class Etat_Contrat(models.Model):
    Designation = models.CharField(max_length=20)

class Poste(models.Model):
    Designation = models.CharField(max_length=30)
    Description = models.TextField(max_length=500)
    
class Employé(models.Model):
    Prénom = models.CharField(max_length=30, null=False, blank=True)
    Nom = models.CharField(max_length=30, null=False, blank=True)
    Date_Naissance = models.DateField(null=True, blank=True)
    Lieu_Naissance = models.CharField(max_length=40, null=True, blank=True)
    Adresse = models.CharField(max_length=60, null=True, blank=True)
    Echelon = models.SmallIntegerField(null=True, blank=True)
    Categorie = models.SmallIntegerField(null=True, blank=True)
    Salaire_de_Base = models.DecimalField(max_digits=8, decimal_places=3, null=False, blank=True)
    CIN = models.CharField(max_length=8, null=False, blank=True)
    Id_Banque = models.ForeignKey(Banque, on_delete=models.CASCADE, null=True, blank=True)
    Id_Local = models.ForeignKey(Local, on_delete= models.CASCADE, null=True, blank=True)
    Id_Poste = models.ForeignKey(Poste, on_delete= models.CASCADE, null=True, blank=True)
    Id_Etat_Contrat = models.ForeignKey(Etat_Contrat, on_delete= models.CASCADE, null=True, blank=True)