from msilib.schema import ListView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from Discos.models import Discos, Genero
from django.http import HttpResponse
from .discos_forms import Discosformularios
from django.views.generic import ListView, UpdateView
from django.views.generic import DetailView, CreateView

def render_view_discos(request):
    discos=Discos.objects.all()
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

class Discoslist(ListView):
    model=Discos
    template_name = 'discos_list.html'

class Discosdetalle(DetailView):
    model=Discos
    template_name = 'discos_detail.html'

def eliminar_disco(request, disco_nombre):
    disco=Discos.objects.get(nombre=disco_nombre)
    disco.delete()
    disco= Discos.objects.all() 
    return render(request, 'Discos/leerdiscos.html', {'disco':disco})

class Editardiscos(UpdateView):
    model=Discos
    success_url= reverse_lazy('editar_disco')
    fields=['nombre', 'year', 'duration']



