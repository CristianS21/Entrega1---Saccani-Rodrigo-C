from django.http import HttpResponse
from app_agenda.models import Mascota
from django.shortcuts import render, HttpResponse


# Create your views here.
def inicio (request):
    return render (request, "app_agenda/template_1.html")
