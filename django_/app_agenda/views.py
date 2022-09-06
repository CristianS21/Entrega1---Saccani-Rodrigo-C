from django.http import HttpResponse
from app_agenda.models import Mascota
from django.shortcuts import render, HttpResponse


# Create your views here.
def inicio (request):
    return render (request, "app_agenda/plantilla_base.html")


def usuario (request):
    return render (request, "app_agenda/plantilla_1.html")

def mascotas (request):
    return render (request, "app_agenda/plantilla_2.html")

def plantas (request):
    return render (request, "app_agenda/plantilla_3.html")
