from django.urls import path
from app_agenda import views

urlpatterns = [
  
    path('probando/', views.probar_template),
    
]
