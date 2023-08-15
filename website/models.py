from django.db import models

class Employee(models.Model):
    First = models.CharField(max_length=20  , default= "Something")
    Last =  models.CharField(max_length=20  , default= "Something")
    Email = models.EmailField(max_length=60 , default= "Something")
    Salary = models.DecimalField(max_digits=12, decimal_places=3, default= 0)