from django.shortcuts import render
from .models import Event


def event_list(request):
    events = Event.objects.order_by('id')
    return render(request, 'trainerapp/event_list.html', {'events': events})
