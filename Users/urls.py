from django.urls import path
from .views import create_user, edit_user, request_login, logout_view
from django.conf import Settings

urlpatterns = [
    path("login/", request_login, name="Login"),
    path('nuevo_usuario/', create_user, name='AltaUsuario'),
    path('edicion_usuario/', edit_user, name='EdicionUsuario'),
    path('logout/', logout_view , name='Logout'),
]
