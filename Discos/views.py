from django.http import HttpResponse
from django.shortcuts import render
from Discos.models import Discos, Genero
from django.http import HttpResponse
from discos_forms import Discosformularios

# Create your views here.

def render_view_discos(request):
    discos=Discos.object.all()
    if len(discos) == 0: 
        return HttpResponse('El artista seleccionado no tiene discos')
    else:
        return HttpResponse(discos[0].nombre)


def formulario_disco(request):
    if request.method == 'POST':
        form_discos=Discosformularios(request.POST)
        print(form_discos)
        if form_discos.is_valid:
            informacion=form_discos.cleaned_data
            formulario=Discos(nombre=informacion['nombre_de_album'], anio=informacion['year_lanzamiento'])
            formulario.save()
            return render(request, 'Discos\template_discos\template_discos.html')
    else: 
        form_discos=Discosformularios()
    return render(request,'Discos/template_discos/template_discos.html'), {'form_discos':form_discos}
   


def busqueda_discos(request):
    return render(request, 'Discos/template_discos/busqueda_discos.html')

def buscar(request):
    respuesta=f'Estoy buscando el disco nombre: {request.GET[Discos.nombre]}'
    return HttpResponse(respuesta)