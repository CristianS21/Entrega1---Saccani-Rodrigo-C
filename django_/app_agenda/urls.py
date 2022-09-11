from django.urls import path
from app_agenda import views

urlpatterns = [
  
    path('inicio/', views.inicio,name="inicio"),
    #path('usuario/', views.usuario),
    
    # URLs de Mascota! 
    path('mascotas/', views.mascotas, name="Mascota"),
    path('form_mascotas/', views.formulario_mascota, name="form_mascotas"),
    path('busqueda_mascotas/', views.busqueda_mascotas, name="busqueda_mascotas"),
    path('buscar_mascotas/', views.buscar_mascotas, name="buscar_mascota"),
    path('eliminar_item_mascota/<nombre>/', views.eliminar_item_mascota, name="eliminar_item_mascota"),
    
    # URLs de Planta! 
    
    path('plantas/', views.plantas, name="Plantas"),  
    path('form_plantas/', views.formulario_plantas, name="form_plantas"),  
    path('busqueda_plantas/', views.busqueda_plantas, name="busqueda_plantas"),
    path('buscar_plantas/', views.buscar_plantas, name="buscar_planta"),
    path('eliminar_item_planta/<especie>/', views.eliminar_item_planta, name="eliminar_item_planta"),
    

 
    
    
]
