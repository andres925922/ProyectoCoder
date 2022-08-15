from django.urls import path
from Discos.views import *

urlpatterns = [
    # Read
    path('', Discoslist.as_view(), name="discos-list"),
    path('/<pk>', Discosdetalle.as_view(), name='discos-detail'),

    # Create
    path('formulariodisco/', formulario_disco, name='discosformulario'),
    
    # Delete
    path('eliminardisco/<id_disco>', eliminar_disco, name='eliminardisco'),

    # Update
    path('editar/<id_disco>', editar_disco, name='disco_editar'),

    # TODO: Ordenar los de abajo
    path('busquedadiscos/', busqueda_discos),
    path('buscar/', buscar),
    path('', Discoslist.as_view(),name='discos_lista'),

    # generos

    path('generos/', get_all_generos, name="ver_generos"),
    path('alta_generos/', create_genero, name='crear_genero'),
    path('editar_genero/<id>', update_genero, name='editar_genero'),
    path('eliminar_genero/<id>', delete_genero, name='eliminar_genero'),
]