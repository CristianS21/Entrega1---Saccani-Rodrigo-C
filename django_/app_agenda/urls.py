from django.urls import path
from app_agenda import views

urlpatterns = [
  
    path('inicio/', views.inicio,name="inicio"),
    #path('usuario/', views.usuario),
    path('mascotas/', views.mascotas, name="Mascota"),
    path('plantas/', views.plantas, name="Plantas"),  
    path('form_mascotas/', views.formulario_mascota, name="form_mascotas"),
    path('form_plantas/', views.formulario_plantas, name="form_plantas"),
    #path('busc_mascota/', views.busc_mascota),
    #path('buscar/', views.buscar, name="buscar")    
]
