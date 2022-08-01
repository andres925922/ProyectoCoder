from ..models import Room, Message
from django import forms
# from django.forms import ModelForm, Form

class Room_Form(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['users', 'messages']

class Message_Form(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'body',
            'sender'
        ]
        
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

        self.fields['sender'].widget.attrs.update({
            'class' : 'form-select d-none'
        })

        self.fields['body'].widget.attrs.update({
            'class': 'form-control',
            'label': '',
            'value': '' })
    

class New_Room_Form(forms.Form):
    userid = forms.IntegerField(required=True)

