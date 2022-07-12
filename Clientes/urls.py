from django.urls import path
from .views import render_view_clientes

urlpatterns = [
    path('', render_view_clientes),
]