from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario (models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    dni= models.IntegerField()
    email=models.EmailField()
    
class Mascota (models.Model):
    nombre= models.CharField(max_length=30)
    especie= models.CharField(max_length=30)
    sexo = models.CharField(max_length=30)
    fecha_de_nacimiento= models.DateField()

class Posteo (models.Model):
    ciudad=models.CharField(max_length=60)
    pais=models.CharField(max_length=40)
    imagen=models.ImageField(upload_to='imagenes', null=True)
    fecha=models.DateField()
    autor=models.CharField(max_length=250)
    descripcion= models.CharField(max_length=250)
    
class Planta (models.Model):
    especie= models.CharField(max_length=30)
    fecha_de_adopcion= models.DateField()

class Avatar(models.Model):
    # Vinculo con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # Subcaperta avatares de media :)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user}"

