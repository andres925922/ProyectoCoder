from django.urls import path
from Discos.views import *


urlpatterns = [
    path('', render_view_discos, name="ver_discos"),
    path('formulario_disco/', formulario_disco),
    path('busquedadiscos/', busqueda_discos),
    path('buscar/', buscar),
    path('listadiscos/', Discoslist.as_view(),name='discos_lista'),

    # generos

    path('generos/', get_all_generos, name="ver_generos"),
    path('alta_generos/', create_genero, name='crear_genero'),
    path('editar_genero/<id>', update_genero, name='editar_genero'),
    path('eliminar_genero/<id>', delete_genero, name='eliminar_genero'),
]