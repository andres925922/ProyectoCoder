from django import forms
from .models import Discos

class Discosformularios(forms.ModelForm):

    class Meta:

        model = Discos
        fields = ['nombre', 'year', 'duration', 'banda', 'portada']