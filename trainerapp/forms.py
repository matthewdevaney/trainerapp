
from django.forms import inlineformset_factory, ModelForm
from .models import Attendee, Event


class AttendeeForm(ModelForm):
    class Meta:
        model = Attendee
        exclude = ()


AttendeeFormSet = inlineformset_factory(Event, Attendee, form=AttendeeForm, extra=1)
