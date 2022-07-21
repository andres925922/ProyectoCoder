from django.urls import path
from .views import request_login

urlpatterns = [
    path("login/", request_login, name="Login"),
]