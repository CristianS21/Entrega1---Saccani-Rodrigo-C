from django.urls import path
from app_agenda import views

urlpatterns = [
  
    path('', views.inicio,name="inicio"),
    #path('usuario/', views.usuario),
    
    # URLs de posteos de ANIMALES! 
    path('p_animal/', views.p_animal, name="p_animal"),
    path('form_animales/', views.formulario_animales, name="form_animales"),
    path('busqueda_animales/', views.busqueda_animales, name="busqueda_animales"),
    path('buscar_animales/', views.buscar_animales, name="buscar_animales"),
    path('eliminar_item_animales/<int:id>/', views.eliminar_item_animales, name="eliminar_item_animales"),
    path('editar_item_animales/<int:id>/', views.editar_item_animales, name="editar_item_animales"),
    
    # URLs de Planta! 
    
    path('plantas/', views.plantas, name="Plantas"),  
    path('form_plantas/', views.formulario_plantas, name="form_plantas"),  
    path('busqueda_plantas/', views.busqueda_plantas, name="busqueda_plantas"),
    path('buscar_plantas/', views.buscar_plantas, name="buscar_planta"),
    path('eliminar_item_planta/<especie>/', views.eliminar_item_planta, name="eliminar_item_planta"),
    path('editar_item_planta/<especie>/', views.editar_item_planta, name="editar_item_planta"),
    

    
   
    # URLs de Usuario!
    
    path('login/', views.login_request, name='Login'),
    path('registro/', views.registro, name = 'registro'),
    path('logout/', views.CustomLogoutView.as_view(), name = 'logout'),

    # URLs de Perfil!
    path('editar-perfil/', views.ProfileUpdateView.as_view(), name="editar_perfil"),
    path('agregar-avatar/', views.agregar_avatar, name="agregar_avatar"),   

    path('acerca_de_mi/', views.acerca, name="acerca"),
    path('contacto/', views.contacto, name="contacto"),



]

