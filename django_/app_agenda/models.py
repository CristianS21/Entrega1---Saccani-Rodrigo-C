from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posteo_animales (models.Model):
    ciudad=models.CharField(max_length=60)
    pais=models.CharField(max_length=40)
    imagen=models.ImageField(upload_to='imagenes', null=True)
    fecha=models.DateField()
    autor=models.CharField(max_length=60)
    descripcion= models.CharField(max_length=200, blank=True)

class Posteo_plantas (models.Model):
    ciudad=models.CharField(max_length=60)
    pais=models.CharField(max_length=40)
    imagen=models.ImageField(upload_to='imagenes', null=True)
    fecha=models.DateField()
    autor=models.CharField(max_length=60)
    descripcion= models.CharField(max_length=200, blank=True)
    
class Posteo_interacciones (models.Model):
    ciudad=models.CharField(max_length=60)
    pais=models.CharField(max_length=40)
    imagen=models.ImageField(upload_to='imagenes', null=False)
    fecha=models.DateField()
    autor=models.CharField(max_length=60)
    descripcion= models.CharField(max_length=200, blank=True)    


class Avatar(models.Model):
    # Vinculo con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # Subcaperta avatares de media :)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user}"

