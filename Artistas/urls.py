from django.urls import path

from Artistas.services.service_bandas import delete_banda
from .views import (
render_view_artistas, render_view_bandas, render_view_editar_artista, render_view_formulario_artistas, render_view_formulario_bandas,
render_view_artista_detalle, render_view_update_bandas, view_delete_banda
)


urlpatterns = [

    # Views Artistas

    path('', render_view_artistas, name="all_artistas"),
    path('<int:id>', render_view_artista_detalle, name="artista_detalle"),
    path('alta/', render_view_formulario_artistas, name="alta_artista"),
    path('modificacion/<int:id>', render_view_editar_artista, name="editar_artista"),

    # Views Bandas

    path('view_bandas', render_view_bandas, name='list_bandas'),
    path('alta_banda/', render_view_formulario_bandas, name= 'alta_bandas'),
    path('update_banda/<int:id_banda>', render_view_update_bandas, name='update_banda'),
    path('delete_banda/<int:id_banda>', view_delete_banda, name='delete_banda'),
]