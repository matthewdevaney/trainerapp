from django.contrib import admin
from .models import Attendee, Course, Event, Student


@admin.register(Attendee)
class AdminAttendee(admin.ModelAdmin):
    list_display = ['id', 'event', 'student', 'attended']
    fields = ['event_id', 'course_id', 'attended']


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'hours', 'inactive']
    fields = ['title', 'description', 'hours', 'inactive']


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    list_display = ['id', 'course_id', 'location', 'capacity', 'start_datetime', 'end_datetime']
    fields = ['course', ('location', 'capacity'), ('start_datetime', 'end_datetime')]


@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'inactive']
    fields = ['first_name', 'last_name', 'email', 'inactive']

