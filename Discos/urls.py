from django.urls import path
from Discos.views import *


urlpatterns = [
    path('Discos/', render_view_discos, name="ver_discos"),
    path('formulario_disco/', formulario_disco),
    path('busquedadiscos/', busqueda_discos),
    path('buscar/', buscar),
    path('listadiscos/', Discoslist.as_view(),name='discos_lista'),
]