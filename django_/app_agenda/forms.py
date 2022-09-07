from django import forms


class form_mascotas (forms.Form):
    nombre= forms.CharField()
    especie= forms.CharField()
    sexo = forms.CharField()
    fecha_de_nacimiento=forms.DateField()

class form_plantas (forms.Form):
    especie= forms.CharField(max_length=30)
    fecha_de_adopcion= forms.DateField()



