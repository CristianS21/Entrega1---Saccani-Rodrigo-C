from django.urls import path
from app_agenda import views

urlpatterns = [
  
    path('', views.inicio,name="inicio"),
    #path('usuario/', views.usuario),
    
    # URLs de Mascota! 
    path('mascotas/', views.mascotas, name="Mascota"),
    path('form_mascotas/', views.formulario_mascota, name="form_mascotas"),
    path('busqueda_mascotas/', views.busqueda_mascotas, name="busqueda_mascotas"),
    path('buscar_mascotas/', views.buscar_mascotas, name="buscar_mascota"),
    path('eliminar_item_mascota/<nombre>/', views.eliminar_item_mascota, name="eliminar_item_mascota"),
    path('editar_item_mascota/<nombre>/', views.editar_item_mascota, name="editar_item_mascota"),
    
    # URLs de Planta! 
    
    path('plantas/', views.plantas, name="Plantas"),  
    path('form_plantas/', views.formulario_plantas, name="form_plantas"),  
    path('busqueda_plantas/', views.busqueda_plantas, name="busqueda_plantas"),
    path('buscar_plantas/', views.buscar_plantas, name="buscar_planta"),
    path('eliminar_item_planta/<especie>/', views.eliminar_item_planta, name="eliminar_item_planta"),
    path('editar_item_planta/<especie>/', views.editar_item_planta, name="editar_item_planta"),
    
    # URLs de Posteos

    path('posteo/', views.posteo, name="posteo"),
    path('principal/', views.principal, name="principal"),  
   
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

