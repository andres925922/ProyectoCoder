from ..models import Room, Message
from django.forms import ModelForm

class Room_Form(ModelForm):
    class Meta:
        model = Room
        fields = ['topic', 'user']

class Message_Form(ModelForm):
    class Meta:
        model = Message
        fields = [
            'title',
            'body',
            'room',
            'to',
            'from_',
            'read'
        ]