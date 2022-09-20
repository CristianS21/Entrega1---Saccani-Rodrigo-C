from django import forms
from app_agenda.models import Avatar
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class form_mascotas (forms.Form):
    nombre= forms.CharField()
    especie= forms.CharField()
    sexo = forms.CharField()
    fecha_de_nacimiento=forms.DateField()

class form_plantas (forms.Form):
    especie= forms.CharField(max_length=30)
    fecha_de_adopcion= forms.DateField()


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