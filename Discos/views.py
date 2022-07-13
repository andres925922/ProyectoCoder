from django.http import HttpResponse
from django.shortcuts import render
from Discos.models import Disco
from django.http import HttpResponse

# Create your views here.

def render_view_discos(request):
    discos=Disco.object.all()
    if len(discos) == 0: 
        return HttpResponse('El artista seleccionado no tiene discos')
    else:
        return HttpResponse(discos[0].nombre)


def formulario_disco(request):
    return render(request, 'Discos/formulario_discos.html')
    
   
