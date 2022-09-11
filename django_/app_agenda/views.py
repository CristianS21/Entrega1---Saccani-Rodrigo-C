from contextlib import redirect_stderr
from django.http import HttpResponse
from app_agenda.models import Mascota,Planta
from django.shortcuts import render, HttpResponse,redirect,reverse
from typing import Dict
from app_agenda.forms import form_mascotas,form_plantas

# Create your views here.
def inicio (request):
    return render (request, "app_agenda/plantilla_inicio.html")

def usuario (request):
    return render (request, "app_agenda/plantilla_1.html")

# VIEWS de MASCOTAS

def mascotas (request):
    mascotas = Mascota.objects.all()
    contexto= {"mascotas":mascotas}
    borrado= request.GET.get("borrado",None)
    contexto ["borrado"] = borrado    
    return render (request, "app_agenda/plantilla_2.html",contexto)

def eliminar_item_mascota (request,nombre):
    mascota=Mascota.objects.get(nombre=nombre)
    borrado_nombre= mascota.nombre
    mascota.delete()
    url_final= f"{reverse ('Mascota')}?borrado={borrado_nombre}"
  
    return redirect (url_final)

def formulario_mascota (request):
    if request.method =='POST':
        formulario=form_mascotas(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data       

            mascota1 = Mascota (nombre= data ['nombre'],especie= data ['especie'],sexo= data ['sexo'], fecha_de_nacimiento= data ['fecha_de_nacimiento'])
            mascota1.save()
            return render (request, "app_agenda/plantilla_inicio.html")
    else:
        formulario= form_mascotas()
    return render (request, "app_agenda/form_mascota.html",{"formulario":formulario})

def busqueda_mascotas (request):
    return render (request, "app_agenda/busqueda_mascotas.html")

def buscar_mascotas (request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        mascotas= Mascota.objects.filter(nombre=nombre)
        return render (request, "app_agenda/resultado_busqueda_mascotas.html", {"mascotas":mascotas}) 
    else: 
        respuesta= "No enviaste datos"
    return HttpResponse (respuesta)

#VIEWS de PLANTAS

def plantas (request):
    plantas = Planta.objects.all()
    contexto= {"plantas":plantas}
    borrado= request.GET.get("borrado",None)
    contexto ["borrado"] = borrado    
    return render (request, "app_agenda/plantilla_3.html",contexto)

def eliminar_item_planta (request,especie):
    planta=Planta.objects.get(especie=especie)
    borrado_especie= planta.especie
    planta.delete()
    url_final= f"{reverse ('Plantas')}?borrado={borrado_especie}"
  
    return redirect (url_final)

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


def busqueda_plantas (request):
    return render (request, "app_agenda/busqueda_plantas.html")

def buscar_plantas (request):
    if request.GET["especie"]:
        especie=request.GET["especie"]
        plantas= Planta.objects.filter(especie=especie)
        return render (request, "app_agenda/resultado_busqueda_plantas.html", {"plantas":plantas}) 
    else: 
        respuesta= "No enviaste datos"
    return HttpResponse (respuesta)    

