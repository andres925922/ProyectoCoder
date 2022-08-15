from socket import fromshare
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

from Users.models import Avatar

class User_Auth_Form(AuthenticationForm):
    pass


class User_Creation_Form(UserCreationForm):

    username = forms.CharField(label = 'Username')
    email = forms.EmailField(label = 'Email')
    password1 = forms.CharField(label='COntraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    first_name = forms.CharField(label = 'Nombre')
    last_name = forms.CharField(label = 'Apellido')
    

    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = { k : "" for k in fields }

class User_Update_Form(UserCreationForm):

    email = forms.EmailField(label = 'Email')
    password1 = forms.CharField(label='COntraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    first_name = forms.CharField(label = 'Nombre')
    last_name = forms.CharField(label = 'Apellido')
    

    
    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = { k : "" for k in fields }


# class Avatar_form(forms.ModelForm):
#      class Meta:
#         model = Avatar
#         fields = ['img', 'user']



