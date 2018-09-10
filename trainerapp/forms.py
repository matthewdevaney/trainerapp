from django.forms import inlineformset_factory


class EventForm(ModelForm):
    EventFormSet = inlineformset_factory(Attendee, Event, fields=('last_name','first_name','attended',))