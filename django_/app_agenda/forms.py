from django import forms
from app_agenda.models import Avatar
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_agenda.models import Posteo_animales, Posteo_plantas, Posteo_interacciones

class posteo_formulario_animales (forms.Form):
    ciudad= forms.CharField(max_length=60)
    pais= forms.CharField(max_length=40)
    imagen= forms.ImageField()
    fecha=forms.DateField()
    autor=forms.CharField(max_length=60)
    descripcion=forms.CharField(max_length=200)

    class Meta:
        model = Posteo_animales
        fields = ['imagen']

class posteo_formulario_plantas (forms.Form):
    ciudad= forms.CharField(max_length=60)
    pais= forms.CharField(max_length=40)
    imagen= forms.ImageField()
    fecha=forms.DateField()
    autor=forms.CharField(max_length=60)
    descripcion=forms.CharField(max_length=200)
    
    class Meta:
        model = Posteo_plantas
        fields = ['imagen']

class posteo_formulario_interacciones (forms.Form):
    ciudad= forms.CharField(max_length=60)
    pais= forms.CharField(max_length=40)
    imagen= forms.ImageField()
    fecha=forms.DateField()
    autor=forms.CharField(max_length=60)
    descripcion=forms.CharField(max_length=200)
    
    class Meta:
        model = Posteo_interacciones
        fields = ['imagen']



class UserRegisterForm (UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
        'username':None,
        'email':None,
        }


class UserUpdateForm (forms.ModelForm):

    class Meta:
        model = User
        fields = [ 'username', 'email' ]
        help_texts = {
        'username':None,
        'email':None,
        }

class AvatarFormulario (forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']