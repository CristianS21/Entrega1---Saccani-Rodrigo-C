from django.urls import path
from app_agenda import views

urlpatterns = [
  
    path('', views.inicio),
    path('usuario/', views.usuario),
    path('mascotas/', views.mascotas, name="Mascota"),
    path('plantas/', views.plantas,name="Plantas"),    
]
