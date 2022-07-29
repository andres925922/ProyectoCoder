from django.shortcuts import render

from Users.models import Avatar
from Base.services.base_service import get_about

# Create your views here.

def get_avatar(request):
    print("hola")
    return Avatar.objects.filter(user = request.user)[0]

