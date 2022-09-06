from django.urls import path
from app_agenda import views

urlpatterns = [
  
    path('', views.inicio),
    path('usuario/', views.usuario),
    path('mascotas/', views.mascotas),
    path('plantas/', views.plantas),    
]
