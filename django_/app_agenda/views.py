from django.http import HttpResponse
from app_agenda.models import Mascota,Planta
from django.shortcuts import render, HttpResponse
from typing import Dict
from app_agenda.forms import form_mascotas,form_plantas

# Create your views here.
def inicio (request):
    return render (request, "app_agenda/plantilla_inicio.html")

def usuario (request):
    return render (request, "app_agenda/plantilla_1.html")

def mascotas (request):
    return render (request, "app_agenda/plantilla_2.html")


def formulario_mascota (request):
    print ("1")
    if request.method =='POST':
        formulario=form_mascotas(request.POST)
        print ("2")
        if formulario.is_valid():
            data = formulario.cleaned_data       

            mascota1 = Mascota (nombre= data ['nombre'],especie= data ['especie'],sexo= data ['sexo'], fecha_de_nacimiento= data ['fecha_de_nacimiento'])
            mascota1.save()
            return render (request, "app_agenda/plantilla_inicio.html")
            
    else:
        print ("3")
        formulario= form_mascotas()
    return render (request, "app_agenda/form_mascota.html",{"formulario":formulario})


def buscar_mascota (request):
    mascotas= Mascota.objects.all()
    return render (request,"app_agenda/plantilla_2.html", {"mascotas":mascotas})



def formulario_plantas (request):
    if request.method =='POST':
        formulario=form_plantas(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data       

            mascota1 = Planta (especie= data ['especie'], fecha_de_adopcion=data ['fecha_de_adopcion'])
            mascota1.save()
            return render (request, "app_agenda/plantilla_inicio.html")
    else:
        formulario= form_plantas()
    return render (request, "app_agenda/form_plantas.html",{"formulario":formulario})
        
def buscar_planta (request):
    plantas= Planta.objects.all()
    return render (request,"app_agenda/plantilla_3.html", {"plantas":plantas})



def plantas (request):
    return render (request, "app_agenda/plantilla_3.html")
