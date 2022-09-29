
from django.http import HttpResponse
from app_agenda.models import Posteo_animales, Posteo_plantas, Posteo_interacciones 
from django.shortcuts import render, HttpResponse, redirect, reverse 
from app_agenda.forms import posteo_formulario_animales, posteo_formulario_plantas, UserRegisterForm, UserUpdateForm, AvatarFormulario, posteo_formulario_interacciones
from django.views.generic import UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy



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
    posteos_a = Posteo_animales.objects.all()
    contexto= {"posteos":posteos_a}
    borrado= request.GET.get("borrado",None)
    contexto ["borrado"] = borrado   
    return render (request, "app_agenda/plantilla_2.html", contexto)

@login_required
def eliminar_item_animales (request,id):
    print("0")
    posteo = Posteo_animales.objects.get (id=id)
    print("1")
    borrado_id= posteo.ciudad
    print("2")
    posteo.delete()
    print ("4")
    url_final= f"{reverse ('p_animal')}?borrado={borrado_id}"
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

    else:  
        formulario= posteo_formulario_animales()  # Formulario vacio para construir el html
    return render(request, "app_agenda/form_posteo_a.html", {"formulario": formulario})
    
@login_required
def busqueda_animales (request):
    return render (request, "app_agenda/busqueda_animales.html")

@login_required
def buscar_animales(request):
    if request.GET["ciudad"]:
        print ("1")
        ciudad=request.GET["ciudad"]
        print ("2")
        animales= Posteo_animales.objects.filter(ciudad=ciudad)
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
            
            data = formulario.cleaned_data

            animal_edit.imagen = data['imagen']
            animal_edit.ciudad = data['ciudad']
            animal_edit.pais = data['pais']
            animal_edit.fecha = data['fecha']
            animal_edit.autor = data ['autor']
            animal_edit.descripcion = data ['descripcion']
            animal_edit.save()
          
            return redirect (reverse ('p_animal'))

    else:  # GET
  
        inicial = {

            'imagen': animal_edit.imagen,
            'ciudad': animal_edit.ciudad,
            'pais': animal_edit.pais,
            'fecha': animal_edit.fecha,
            'autor': animal_edit.autor,
            'descripcion': animal_edit.descripcion,
        }
        formulario = posteo_formulario_animales (initial=inicial)
    return render (request, "app_agenda/editar_form.html", {"formulario": formulario})



#VIEWS de POSTEO PLANTAS
@login_required
def p_plantas (request):
    posteos = Posteo_plantas.objects.all()
    contexto= {"posteos":posteos}
    borrado= request.GET.get("borrado",None)
    contexto ["borrado"] = borrado    
    return render (request, "app_agenda/plantilla_3.html",contexto)

@login_required
def eliminar_item_plantas (request,id):
    posteo= Posteo_plantas.objects.get(id=id)
    borrado_id= posteo.ciudad
    posteo.delete()
    url_final= f"{reverse ('p_plantas')}?borrado={borrado_id}"
  
    return redirect (url_final)

@login_required
def formulario_plantas (request):
    if request.method =='POST':

        formulario= posteo_formulario_plantas (request.POST,request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            posteo1= Posteo_plantas (imagen= data ['imagen'],ciudad=data ['ciudad'],pais = data ['pais'],fecha =data['fecha'], autor=data['autor'], descripcion=data['descripcion'], )
            posteo1.save()
     
            return render (request, "app_agenda/plantilla_inicio.html")
        #return render(request, "app_agenda/plantilla_principal.html")
    else:  
        formulario= posteo_formulario_plantas()  # Formulario vacio para construir el html
    return render(request, "app_agenda/form_posteo_p.html", {"formulario": formulario})

@login_required
def busqueda_plantas (request):
    return render (request, "app_agenda/busqueda_plantas.html")

@login_required
def buscar_plantas (request):
    if request.GET["ciudad"]:
        ciudad=request.GET["ciudad"]
        plantas= Posteo_plantas.objects.filter(ciudad=ciudad)
        return render (request, "app_agenda/resultado_busqueda_plantas.html", {"plantas":plantas}) 
    else: 
        respuesta= "Error, no enviaste formulario"
    return render (request, "app_agenda/buscar_p_error.html",{"respuesta":respuesta} ) 

@login_required
def editar_item_plantas (request, id):
    planta_edit = Posteo_plantas.objects.get(id=id)
 
    if request.method == 'POST':
        formulario = posteo_formulario_plantas (request.POST,request.FILES)
     
        if formulario.is_valid():
            data = formulario.cleaned_data

            planta_edit.imagen = data['imagen']
            planta_edit.ciudad = data['ciudad']
            planta_edit.pais = data['pais']
            planta_edit.fecha = data['fecha']
            planta_edit.autor = data ['autor']
            planta_edit.descripcion = data ['descripcion']
            planta_edit.save()
            print ("3")
            return redirect (reverse ('p_plantas'))

    else:  # GET
        print("0")    
        inicial = {
            'imagen': planta_edit.imagen,
            'ciudad': planta_edit.ciudad,
            'pais': planta_edit.pais,
            'fecha': planta_edit.fecha,
            'autor': planta_edit.autor,
            'descripcion': planta_edit.descripcion,
        }
        formulario = posteo_formulario_plantas (initial=inicial)
    return render (request, "app_agenda/editar_form.html", {"formulario": formulario})

# VIEWS de INTERACCIONES
@login_required
def p_interacciones (request):
    posteos = Posteo_interacciones.objects.all()
    contexto= {"posteos":posteos}
    borrado= request.GET.get("borrado",None)
    contexto ["borrado"] = borrado    
    return render (request, "app_agenda/plantilla_4.html",contexto)

@login_required
def formulario_interacciones (request):
    if request.method =='POST':

        formulario= posteo_formulario_interacciones (request.POST, request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            posteo= Posteo_interacciones (imagen= data ['imagen'],ciudad=data ['ciudad'],pais = data ['pais'],fecha =data['fecha'], autor=data['autor'], descripcion=data['descripcion'], )
            posteo.save()
     
            return render (request, "app_agenda/plantilla_inicio.html")
        #return render(request, "app_agenda/plantilla_principal.html")
    else:  
        formulario= posteo_formulario_interacciones()  # Formulario vacio para construir el html
    return render(request, "app_agenda/form_posteo_i.html", {"formulario": formulario})
    
def busqueda_interacciones (request):
    return render (request, "app_agenda/busqueda_interacciones.html")

@login_required
def buscar_interacciones (request):
    
    if request.GET["ciudad"]:
        
        ciudad=request.GET["ciudad"]
        
        interacciones= Posteo_interacciones.objects.filter(ciudad=ciudad)
        return render (request, "app_agenda/resultado_busqueda_interacciones.html", {"interacciones":interacciones}) 
    else: 
        respuesta= "Error, no enviaste formulario"
    return render (request, "app_agenda/buscar_p_error.html",{"respuesta":respuesta} ) 

@login_required
def editar_item_interacciones (request, id):
    interaccion_edit = Posteo_interacciones.objects.get(id=id)
 
    if request.method == 'POST':
        formulario = posteo_formulario_interacciones (request.POST,request.FILES)

        if formulario.is_valid():
            data = formulario.cleaned_data

            interaccion_edit.imagen = data['imagen']
            interaccion_edit.ciudad = data['ciudad']
            interaccion_edit.pais = data['pais']
            interaccion_edit.fecha = data['fecha']
            interaccion_edit.autor = data ['autor']
            interaccion_edit.descripcion = data ['descripcion']
            interaccion_edit.save()
            print ("3")
            return redirect (reverse ('p_interacciones'))

    else:  # GET
        print("0")    
        inicial = {
            'imagen': interaccion_edit.imagen,
            'ciudad': interaccion_edit.ciudad,
            'pais': interaccion_edit.pais,
            'fecha': interaccion_edit.fecha,
            'autor': interaccion_edit.autor,
            'descripcion': interaccion_edit.descripcion,
        }
        formulario = posteo_formulario_interacciones(initial=inicial)
    return render (request, "app_agenda/editar_form.html", {"formulario": formulario})

@login_required
def eliminar_item_interacciones (request,id):
    posteo= Posteo_interacciones.objects.get(id=id)
    borrado_id= posteo.ciudad
    posteo.delete()
    url_final= f"{reverse ('p_interacciones')}?borrado={borrado_id}"
  
    return redirect (url_final)

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
                return render(request, "app_agenda/respuesta_login.html", {"gracias":f"Ya podés ingresar a los posteos!!!"})
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
            return render(request, "app_agenda/respuesta_registro.html", {"mensaje": "Usuario Creado :)"})
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
        if form.is_valid():   #Si pasó la validación de Django
            avatar = form.save()
            avatar.user = request.user
            avatar.save()
            return redirect(reverse('inicio'))
    form = AvatarFormulario() #Formulario vacio para construir el html
    return render(request, "app_agenda/form_avatar.html", {"form":form})

@login_required  
def datos_usuario (request):
    return render (request, "app_agenda/datos_usuario.html")

