from django.shortcuts import render
from .models import Course, Event, Student
from datetime import datetime


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
