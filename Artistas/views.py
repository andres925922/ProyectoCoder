from django.shortcuts import render
from .services.service_artistas import (
get_all_artistas, 
get_artista_por_nombre_y_apellido
)
from .forms.forms import Artista_Formulario, Banda_Formulario
from .models import Artista, Banda
# Create your views here.

def render_view_artistas(request):
    
    return render(
        request = request,
        template_name='Artistas/template_artistas.html',
        context= {
            'artistas': get_all_artistas()
        }
    )

def render_view_formulario_bandas(request):
    if request.method == "POST":
        formulario = Banda_Formulario(request.POST)
        if formulario.is_valid:
            info = formulario.cleaned_data
            print(info)
            banda = Banda(
                nombre = info['nombre']
            )
            banda.save()
            return render(request, 'Artistas/template_artistas.html', context= {
                'artistas': get_all_artistas()
            })
    else:
        formulario = Banda_Formulario()

    return render(request, 'Artistas/formulario_banda.html', {'form' : formulario})

def render_view_formulario_artistas(request):

    if request.method == 'POST':
        formulario = Artista_Formulario(request.POST)
        if formulario.is_valid:
            info = formulario.cleaned_data
            artista = Artista(
                nombre = info['nombre'],
                apellido = info['apellido'],
                nombre_artistico = info['nombre_artistico'],
                banda = info['banda']
            )
            artista.save()
            return render(request, 'Artistas/template_artistas.html', context= {
                'artistas': get_all_artistas()
            })

    else:
        formulario = Artista_Formulario()

    return render(request, 'Artistas/formulario_artista.html', {'form' : formulario})

def render_artista_por_nombre_y_apellido(request):
    pass