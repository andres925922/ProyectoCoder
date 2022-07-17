from django import forms

class Discosformularios(forms.Form):
    nombre_de_album=forms.CharField()
    year_lanzamiento=forms.IntegerField()