from django.forms import ModelForm
from .models import Attendee


class AttendeeForm(ModelForm):
    class Meta:
        model = Attendee


