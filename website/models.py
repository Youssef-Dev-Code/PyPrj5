from django.db import models

class Employee(models.Model):
    def __init__(self):
        First = models.CharField(max_length=20)
        Last =  models.CharField(max_length=20)
        Email = models.EmailField(max_length=60)
        CIN = models.CharField(max_length=8)
        Date_Naissance = models.DateField()
        Salary = models.DecimalField(max_digits=12, decimal_places=3)