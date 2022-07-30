from ..models import Room, Message
from django.forms import ModelForm

class Room_Form(ModelForm):
    class Meta:
        model = Room
        fields = ['users', 'messages']

class Message_Form(ModelForm):
    class Meta:
        model = Message
        fields = [
            'body',
            'sender'
        ]

