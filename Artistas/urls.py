from django.urls import path
from .views import render_view_artistas, render_view_formulario_artistas, render_view_formulario_bandas

urlpatterns = [
    path('', render_view_artistas),
    path('alta/', render_view_formulario_artistas),
    path('alta_banda/', render_view_formulario_bandas),
]