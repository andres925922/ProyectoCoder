from django.http import HttpResponse
from django.shortcuts import render
from Discos.models import Disco
from django.http import HttpResponse



# Create your views here.

def render_view_discos(request):
    discos=Disco.object.all()
    if len(discos) == 0: 
        return render, HttpResponse('El artista seleccionado no tiene discos')
    else:
        return render, HttpResponse(f'Nombre del disco: {Disco.nombre}')


def guardar_discos(request):
    nombre_disco1=Disco(nombre='Dropout Boogie')
    nombre_disco1.save()
    return HttpResponse(f'El disco se llama: {nombre_disco1}')

    
   
