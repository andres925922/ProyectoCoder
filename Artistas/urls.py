from django.urls import path
from .views import render_view_artistas, render_view_formulario_artistas

urlpatterns = [
    path('', render_view_artistas),
    path('form/', render_view_formulario_artistas),

]