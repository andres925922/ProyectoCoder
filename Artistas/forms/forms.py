from dataclasses import fields
from django import forms

from Artistas.models import Artista, Banda
from ..services.service_bandas import get_all_bandas

# class Artista_Formulario(forms.Form):
#     nombre = forms.CharField(max_length=50)
#     apellido = forms.CharField(max_length=75)
#     nombre_artistico = forms.CharField(max_length=50)
#     banda = forms.ModelChoiceField(
#         queryset=get_all_bandas()
#     )

# class Banda_Formulario(forms.Form):
#     nombre = forms.CharField(max_length=50)

class Artista_Formulario(forms.ModelForm):

    class Meta:
        model = Artista
        fields = ['nombre', 
        'apellido', 
        'nombre_artistico', 
        'banda', 
        'historia', 
        'imagen']

    def clean(self):
        print(self.cleaned_data)
        return self.cleaned_data

class Banda_Formulario(forms.ModelForm):

    class Meta:
        model = Banda
        fields = ['nombre', 'historia_banda', 'imagen']
