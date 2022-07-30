from django.urls import path
from .views import (
    create_user, 
    edit_user,
    get_conversation, 
    request_login, 
    logout_view,
    get_room
)
from django.conf import Settings

urlpatterns = [
    path("login/", request_login, name="Login"),
    path('nuevo_usuario/', create_user, name='AltaUsuario'),
    path('edicion_usuario/', edit_user, name='EdicionUsuario'),
    path('logout/', logout_view , name='Logout'),
    path('messenger/', get_room, name='Mensajes'),
    path('room/<int:pk>/<int:to>', get_conversation, name='detailed'),
    path('nuevo_mensaje', request_login, name="newMsg")
]
