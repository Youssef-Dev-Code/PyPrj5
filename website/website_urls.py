from django.urls import path
from .views import *
urlpatterns = [
    path(route="", view= index, name="index"),
    path(route="Créer_Employé/", view= Créer_Employé, name="Emp_Créer")
]
