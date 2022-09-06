from django.db import models

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


class Planta (models.Model):
    especie= models.CharField(max_length=30)
    fecha_de_adopcion= models.DateField()

