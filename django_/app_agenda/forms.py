from django import forms
from app_agenda.models import Avatar
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_agenda.models import Posteo_animales

class form_plantas (forms.Form):
    especie= forms.CharField(max_length=30)
    fecha_de_adopcion= forms.DateField()


class posteo_formulario_animales (forms.Form):
    id = forms.IntegerField()
    ciudad= forms.CharField(max_length=60)
    pais= forms.CharField(max_length=40)
    imagen= forms.ImageField()
    fecha=forms.DateField()
    autor=forms.CharField(max_length=250)
    descripcion=forms.CharField(max_length=250)

    class Meta:
        model = Posteo_animales
        fields = ['imagen']

class UserRegisterForm (UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = [  'first_name','last_name', 'username', 'email', 'password1', 'password2']
        help_texts = {'first_name': None,
        'last_name':None,
        'username':None,
        'email':None,
        }


class UserUpdateForm (forms.ModelForm):

    class Meta:
        model = User
        fields = [ 'first_name','last_name','username', 'email' ]
        help_texts = {'first_name': None,
        'last_name':None,
        'username':None,
        'email':None,
        }

class AvatarFormulario (forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']