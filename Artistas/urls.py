from django.urls import path
from .views import (
render_view_artistas, render_view_editar_artista, render_view_formulario_artistas, render_view_formulario_bandas,
render_view_artista_detalle
)

urlpatterns = [
    path('', render_view_artistas, name="all_artistas"),
    path('/<int:id>', render_view_artista_detalle, name="artista_detalle"),
    path('alta/', render_view_formulario_artistas, name="alta_artista"),
    path('modificacion/<int:id>', render_view_editar_artista, name="editar_artista"),
    path('alta_banda/', render_view_formulario_bandas),
]