from django import forms
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
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']
