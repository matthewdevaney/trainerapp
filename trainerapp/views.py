from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Attendee, Course, Event, Student
from datetime import datetime


class AttendeeAdd(CreateView):
    model = Attendee
    fields = '__all__'
    template_name_suffix = '_add_form'

    def get_initial(self):
        initial = super(AttendeeAdd, self).get_initial()
        initial['event'] = self.request.GET.get('event_id', None)
        return initial

    def get_success_url(self):
        next_url = self.request.POST.get('next', None)
        if next_url:
            return next_url


class AttendeeEdit(UpdateView):
    model = Attendee
    fields = ['attended']
    template_name_suffix = '_edit_form'

    def get_success_url(self):
        return reverse_lazy('event_detail', kwargs={'pk': self.object.event.id})


class AttendeeDelete(DeleteView):
    model = Attendee

    def get_success_url(self):
        return reverse_lazy('event_detail', kwargs={'pk': self.object.event.id})


class CourseAdd(CreateView):
    model = Course
    fields = '__all__'
    template_name_suffix = '_add_form'


class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('course_list')


class CourseDetail(generic.DetailView):
    model = Course


class CourseEdit(UpdateView):
    model = Course
    fields = '__all__'
    template_name_suffix = '_edit_form'


class EventAdd(CreateView):
    model = Event
    fields = '__all__'
    template_name_suffix = '_add_form'


class EventDetail(generic.DetailView):
    model = Event


class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy('upcoming_event_list')


class EventEdit(UpdateView):
    model = Event
    fields = '__all__'
    template_name_suffix = '_edit_form'


class StudentAdd(CreateView):
    model = Student
    fields = '__all__'
    template_name_suffix = '_add_form'


class StudentDetail(generic.DetailView):
    model = Student


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')


class StudentEdit(UpdateView):
    model = Student
    fields = '__all__'
    template_name_suffix = '_edit_form'


def upcoming_event_list(request):
    events = Event.objects.filter(end_datetime__gt=datetime.now()).order_by('start_datetime')
    return render(request, 'trainerapp/event_list.html', {'events': events, 'table_title': 'Upcoming Events'})


def past_event_list(request):
    events = Event.objects.filter(end_datetime__lt=datetime.now()).order_by('-start_datetime')
    return render(request, 'trainerapp/event_list.html', {'events': events, 'table_title': 'Past Events'})


def course_list(request):
    courses = Course.objects.filter(inactive=False).order_by('id')
    return render(request, 'trainerapp/course_list.html', {'courses': courses, 'table_title': 'Courses'})


def inactive_course_list(request):
    courses = Course.objects.filter(inactive=True).order_by('id')
    return render(request, 'trainerapp/course_list.html', {'courses': courses, 'table_title': 'Inactive Courses'})


def student_list(request):
    students = Student.objects.filter(inactive=False).order_by('last_name', 'first_name', 'id')
    return render(request, 'trainerapp/student_list.html', {'students': students, 'table_title': 'Students'})


def inactive_student_list(request):
    students = Student.objects.filter(inactive=True).order_by('last_name', 'first_name', 'id')
    return render(request, 'trainerapp/student_list.html', {'students': students, 'table_title': 'Inactive Students'})
