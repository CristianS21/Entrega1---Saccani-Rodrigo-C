
from django.http import HttpResponse
from app_agenda.models import Posteo_animales,Planta
from django.shortcuts import render, HttpResponse, redirect, reverse 
from app_agenda.forms import posteo_formulario_animales, form_plantas, UserRegisterForm, UserUpdateForm, AvatarFormulario
from django.views.generic import UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from app_agenda.models import Posteo_animales


def inicio (request):
    return render (request, "app_agenda/plantilla_inicio.html")

@login_required
def usuario (request):
    return render (request, "app_agenda/plantilla_1.html")

def acerca(request):
      return render (request, "app_agenda/acerca.html")

def contacto (request):
      return render (request, "app_agenda/contacto.html")

# VIEWS de POSTEO ANIMALES 

@login_required
def p_animal (request):
    posteos = Posteo_animales.objects.all()
    contexto= {"posteos":posteos}
    borrado= request.GET.get("borrado",None)
    contexto ["borrado"] = borrado   
    return render (request, "app_agenda/plantilla_2.html", contexto)

@login_required
def eliminar_item_animales (request,id):
    print("0")
    posteo = Posteo_animales.objects.get (id=id)
    print("1")
    borrado_ciudad= posteo.id
    print("2")
    posteo.delete()
    print ("4")
    url_final= f"{reverse ('p_animal')}?borrado={borrado_ciudad}"
    return redirect (url_final)

@login_required
def formulario_animales (request):
    if request.method =='POST':

        formulario= posteo_formulario_animales (request.POST,request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            posteo1= Posteo_animales (imagen= data ['imagen'],ciudad=data ['ciudad'],pais = data ['pais'],fecha =data['fecha'], autor=data['autor'], descripcion=data['descripcion'], )
            posteo1.save()
     
            return render (request, "app_agenda/plantilla_inicio.html")
        #return render(request, "app_agenda/plantilla_principal.html")
    else:  
        formulario= posteo_formulario_animales()  # Formulario vacio para construir el html
    return render(request, "app_agenda/form_posteo_a.html", {"formulario": formulario})
    
@login_required
def busqueda_animales (request):
    return render (request, "app_agenda/busqueda_animales.html")

@login_required
def buscar_animales(request):
    if request.GET["id"]:
        print ("1")
        id=request.GET["ciudad"]
        print ("2")
        animales= Posteo_animales.objects.filter(id=id)
        return render (request, "app_agenda/resultado_busqueda_animales.html", {"animales":animales}) 
    else: 
        respuesta= "Error, no enviaste formulario"
    return render (request, "app_agenda/buscar_m_error.html",{"respuesta":respuesta} )

@login_required    
def editar_item_animales (request, id):
    animal_edit = Posteo_animales.objects.get(id=id)

    if request.method == 'POST':
        formulario = posteo_formulario_animales(request.POST, request.FILES)

        if formulario.is_valid():
            print ("0")
            data = formulario.cleaned_data
            animal_edit.id = data['id']
            animal_edit.imagen = data['imagen']
            animal_edit.ciudad = data['ciudad']
            animal_edit.pais = data['pais']
            animal_edit.fecha = data['fecha']
            animal_edit.autor = data ['autor']
            animal_edit.descripcion = data ['descripcion']
            animal_edit.save()
            print ("1")
            return redirect (reverse ('p_animal'))

    else:  # GET
        print ("2")
        inicial = {
            'id':animal_edit.id,
            'imagen': animal_edit.imagen,
            'ciudad': animal_edit.ciudad,
            'pais': animal_edit.pais,
            'fecha': animal_edit.fecha,
            'autor': animal_edit.autor,
            'descripcion': animal_edit.descripcion,
        }
        formulario = posteo_formulario_animales (initial=inicial)
    return render (request, "app_agenda/form_posteo_a.html", {"formulario": formulario})

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
        formulario = form_plantas (initial=inicial)
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
                return render(request, "app_agenda/respuesta_login.html", {"gracias":f"Sentite muy bienvenido!!!"})
            else:
                return render(request,"app_agenda/respuesta_login.html", {"error1":"Revisá los datos ingresados"})
        else:
            return render(request,"app_agenda/respuesta_login.html", {"error1":"Revisá los datos ingresados"})
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

class ProfileUpdateView(UpdateView):

    model = User

    form_class = UserUpdateForm

    success_url = reverse_lazy('inicio')

    template_name = 'app_agenda/registro.html'

    def get_object(self, queryset=None):
        return self.request.user

class CustomLogoutView(LogoutView):
    template_name = 'app_agenda/despedida.html' 

@login_required
def agregar_avatar(request):

    if request.method == 'POST':

        form = AvatarFormulario (request.POST, request.FILES) #aquí me llega toda la información del html

        if form.is_valid:   #Si pasó la validación de Django
            avatar = form.save()
            avatar.user = request.user
            avatar.save()
            return redirect(reverse('inicio'))

    form = AvatarFormulario() #Formulario vacio para construir el html
    return render(request, "app_agenda/form_avatar.html", {"form":form})
