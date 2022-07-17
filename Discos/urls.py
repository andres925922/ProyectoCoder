from django.urls import path
from Discos.views import *


urlpattern= [
    path('Discos/', render_view_discos, name=Discos),
    path('formulario_disco/', formulario_disco),
    path('busquedadiscos/', busqueda_discos),
    path('buscar/', buscar)


]