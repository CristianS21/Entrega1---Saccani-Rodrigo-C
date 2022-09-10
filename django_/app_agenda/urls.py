from django.urls import path
from app_agenda import views

urlpatterns = [
  
    path('inicio/', views.inicio,name="inicio"),
    #path('usuario/', views.usuario),
    path('mascotas/', views.mascotas, name="Mascota"),
    path('plantas/', views.plantas, name="Plantas"),  
    path('form_mascotas/', views.formulario_mascota, name="form_mascotas"),
    path('form_plantas/', views.formulario_plantas, name="form_plantas"),
   
    path('busqueda_mascotas/', views.busqueda_mascotas, name="busqueda_mascotas"),
    path('buscar_mascotas/', views.buscar_mascotas, name="buscar_mascota"),
   
   
    path('busqueda_plantas/', views.busqueda_plantas, name="busqueda_plantas"),
    path('buscar_plantas/', views.buscar_plantas, name="buscar_planta"),

 
    
    
]
