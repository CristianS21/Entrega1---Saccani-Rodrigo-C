
from django.http import HttpResponse
from app_agenda.models import Mascota,Planta
from django.shortcuts import render, HttpResponse, redirect, reverse 
from app_agenda.forms import form_mascotas, form_plantas, UserRegisterForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def inicio (request):
    return render (request, "app_agenda/plantilla_inicio.html")
@login_required
def usuario (request):
    return render (request, "app_agenda/plantilla_1.html")

# VIEWS de MASCOTAS
@login_required
def mascotas (request):
    mascotas = Mascota.objects.all()
    contexto= {"mascotas":mascotas}
    borrado= request.GET.get("borrado",None)
    contexto ["borrado"] = borrado    
    return render (request, "app_agenda/plantilla_2.html", contexto)
@login_required
def eliminar_item_mascota (request,nombre):
    mascota=Mascota.objects.get(nombre=nombre)
    borrado_nombre= mascota.nombre
    mascota.delete()
    url_final= f"{reverse ('Mascota')}?borrado={borrado_nombre}"
    return redirect (url_final)
@login_required
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
@login_required
def busqueda_mascotas (request):
    return render (request, "app_agenda/busqueda_mascotas.html")
@login_required
def buscar_mascotas (request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        mascotas= Mascota.objects.filter(nombre=nombre)
        return render (request, "app_agenda/resultado_busqueda_mascotas.html", {"mascotas":mascotas}) 
    else: 
        respuesta= "Error, no enviaste formulario"
    return render (request, "app_agenda/buscar_m_error.html",{"respuesta":respuesta} )
@login_required    
def editar_item_mascota (request, nombre):
    mascota_edit = Mascota.objects.get(nombre=nombre)

    if request.method == 'POST':
        formulario = form_mascotas(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            mascota_edit.nombre = data['nombre']
            mascota_edit.especie = data['especie']
            mascota_edit.sexo = data['sexo']
            mascota_edit.fecha_de_nacimiento = data ['fecha_de_nacimiento']
            mascota_edit.save()

            return redirect (reverse ('Mascota'))
    else:  # GET
        inicial = {
            'nombre': mascota_edit.nombre,
            'especie': mascota_edit.especie,
            'sexo': mascota_edit.sexo,
            'fecha_de_nacimiento': mascota_edit.fecha_de_nacimiento,
        }
        formulario = form_mascotas (initial=inicial)
    return render (request, "app_agenda/form_mascota.html", {"formulario": formulario})

#VIEWS de PLANTAS
@login_required
def plantas (request):
    plantas = Planta.objects.all()
    contexto= {"plantas":plantas}
    borrado= request.GET.get("borrado",None)
    contexto ["borrado"] = borrado    
    return render (request, "app_agenda/plantilla_3.html",contexto)
@login_required
def eliminar_item_planta (request,especie):
    planta=Planta.objects.get(especie=especie)
    borrado_especie= planta.especie
    planta.delete()
    url_final= f"{reverse ('Plantas')}?borrado={borrado_especie}"
  
    return redirect (url_final)
@login_required
def formulario_plantas (request):
    if request.method =='POST':
        formulario=form_plantas(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data       

            planta1 = Planta (especie= data ['especie'], fecha_de_adopcion=data ['fecha_de_adopcion'])
            planta1.save()
            return render (request, "app_agenda/plantilla_inicio.html")
    else:
        formulario= form_plantas()
    return render (request, "app_agenda/form_plantas.html",{"formulario":formulario})
@login_required
def busqueda_plantas (request):
    return render (request, "app_agenda/busqueda_plantas.html")
@login_required
def buscar_plantas (request):
    if request.GET["especie"]:
        especie=request.GET["especie"]
        plantas= Planta.objects.filter(especie=especie)
        return render (request, "app_agenda/resultado_busqueda_plantas.html", {"plantas":plantas}) 
    else: 
        respuesta= "Error, no enviaste formulario"
    return render (request, "app_agenda/buscar_p_error.html",{"respuesta":respuesta} ) 
@login_required
def editar_item_planta (request, especie):
    planta_edit = Planta.objects.get(especie=especie)

    if request.method == 'POST':
        formulario = form_plantas(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            planta_edit.especie = data['especie']
            planta_edit.fecha_de_adopcion = data['fecha_de_adopcion']
            planta_edit.save()

            return redirect (reverse ('Plantas'))
    else:  # GET
        inicial = {
            'especie': planta_edit.especie,
            'fecha_de_adopción': planta_edit.fecha_de_adopcion,            
        }
        formulario = form_mascotas (initial=inicial)
    return render (request, "app_agenda/form_plantas.html", {"formulario": formulario})

# VIEWS de USUARIO

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            if user:
                login(request=request, user=user)
                return render(request, "app_agenda/plantilla_inicio.html", {"gracias":f"Bienvenido {usuario}"})
            else:
                return render(request,"app_agenda/plantilla_inicio.html", {"error1":"Revisá los datos ingresados"})
        else:
            return render(request,"app_agenda/plantilla_inicio.html", {"error1":"Revisá los datos ingresados"})
    form = AuthenticationForm() # GET
    return render(request,"app_agenda/login.html", {'form':form} )

def registro (request):
    if request.method == 'POST':
        formulario = UserRegisterForm (request.POST)
        if formulario.is_valid():
            formulario.save()
            return render(request, "app_agenda/plantilla_inicio.html", {"mensaje": "Usuario Creado :)"})
    else:
        formulario = UserRegisterForm()  # Formulario vacio para construir el html
    return render(request, "app_agenda/registro.html", {"form":formulario})

class CustomLogoutView(LogoutView):
    template_name = 'app_agenda/logout.html' 