from django.contrib import admin
from .models import Attendee, Course, Event, Student


@admin.register(Attendee)
class AdminAttendee(admin.ModelAdmin):
    fields = ['event_id', 'course_id', 'attended']


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    fields = ['title', 'description', 'hours', 'inactive']


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    fields = ['course_id', ('start_datetime', 'end_datetime'), ('location', 'capacity')]


@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'email', 'inactive']

