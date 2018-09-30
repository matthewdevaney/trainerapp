import csv

from .forms import AttendeeForm, EventForm

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import localtime
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Attendee, Course, Event, Student
from datetime import datetime


class AttendeeAdd(CreateView):

    form_class = AttendeeForm
    template_name = 'trainerapp\\attendee_add_form.html'

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

    form_class = EventForm
    template_name = 'trainerapp\\event_add_form.html'


class EventDetail(generic.DetailView):
    model = Event


class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy('upcoming_event_list')


class EventEdit(UpdateView):

    form_class = EventForm
    model = Event
    template_name_suffix = '_edit_form'

"""
    model = Event
    fields = '__all__'
    template_name_suffix = '_edit_form'
"""


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
    events = Event.objects.filter(end_date__gte=datetime.now()).order_by('start_date', 'start_time')
    return render(request, 'trainerapp/event_list.html', {'events': events, 'table_title': 'Upcoming Events'})


def past_event_list(request):
    events = Event.objects.filter(end_date__lt=datetime.now()).order_by('-start_date', '-start_time')
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


def students_export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'E-mail', 'Inactive'])

    students = Student.objects.filter(inactive=False).values_list('first_name', 'last_name', 'email', 'inactive')
    for student in students:
        writer.writerow(student)

    return response


def courses_export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="courses.csv"'

    writer = csv.writer(response)
    writer.writerow(['Title', 'Description', 'Hours', 'Inactive'])

    courses = Course.objects.filter(inactive=False).values_list('title', 'description', 'hours', 'inactive')
    for course in courses:
        writer.writerow(course)

    return response


def events_export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="events.csv"'

    writer = csv.writer(response)
    writer.writerow(['Course', 'Start Date', 'Start Time', 'End Date', 'End Time', 'Location', 'Capacity'])

    events = Event.objects.all().prefetch_related('course__title').values_list('course__title', 'start_date',
                                                                               'start_time', 'end_date',
                                                                               'end_time', 'location', 'capacity')
    for event in events:
        writer.writerow(event)

    return response


def attendees_export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="attendees.csv"'

    writer = csv.writer(response)
    writer.writerow(['Course', 'Start Date', 'Hours', 'First Name', 'Last Name', 'Attended'])

    attendees = Attendee.objects.filter(attended=True).select_related('event__course__title', 'event__start_date',
                'event__course__hours', 'student__first_name', 'student__last_name').values_list(
                'event__course__title', 'event__start_date', 'event__course__hours',
                'student__first_name', 'student__last_name', 'attended')

    for attendee in attendees:
        modify_attendee = (attendee[0], attendee[1].strftime('%B %#d, %Y'), attendee[2], attendee[3],
                           attendee[4], attendee[5])
        writer.writerow(modify_attendee)

    return response


def reports_list(request):
    return render(request, template_name='trainerapp/report_list.html')