from Discos.models import (
    Discos,
    Canciones,
    Genero,
    Banda
)
from django.forms import ModelForm


class Canciones_Form(ModelForm):

    class Meta:
        model = Canciones
        fields = '__all__'

class Discos_Form(ModelForm):

    class Meta:
        model = Discos
        fields = '__all__'

class Generos_Form(ModelForm):

    class Meta:
        model = Genero
        fields = ['nombre']

