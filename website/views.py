from django.shortcuts import render
from django.http import response, request
from django.contrib import messages
from .models import *

def index(request):
    context = dict()
    return render(request=request, template_name= "index.html", context= context)

def Créer_Employé(request):
    context = dict()
    return  render(request=request, template_name= "Créer_Employé.html", context= context)