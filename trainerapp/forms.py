from django import forms
from django.forms import ModelForm
from .models import Attendee


class AttendeeForm(ModelForm):
    class Meta:
        model = Attendee
        fields = '__all__'
        widgets = {
            'event': forms.TextInput(attrs={'hidden': True, 'readonly': True}),
        }





