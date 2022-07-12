from django import forms
from ..services.service_bandas import get_all_bandas

class Artista_Formulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=75)
    nombre_artistico = forms.CharField(max_length=50)
    banda = forms.ModelChoiceField(
        queryset=get_all_bandas()
    )