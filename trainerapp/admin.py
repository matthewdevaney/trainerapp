from django.contrib import admin
from .models import Attendee, Course, Event, Student


@admin.register(Attendee)
class AdminAttendee(admin.ModelAdmin):
    list_display = ['id', 'event_description', 'event_datetime', 'student_name', 'attended']
    ordering = ['id']
    fields = ['event', 'student', 'attended']

    def event_description(self, obj):
        return obj.event.course

    def event_datetime(self, obj):
        return obj.event.start_datetime.strftime('%B %#d, %Y @ %#I%p')

    def student_name(self, obj):
        return "".join([obj.student.last_name, ', ', obj.student.first_name])


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'hours', 'inactive']
    ordering = ['id']
    fields = ['title', 'description', 'hours', 'inactive']


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    list_display = ['id', 'course_name', 'location', 'capacity', 'start_datetime', 'end_datetime']
    ordering = ['id']
    fields = ['course', ('location', 'capacity'), ('start_datetime', 'end_datetime')]

    def course_name(self, obj):
        return obj.course.title


@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'inactive']
    ordering = ['id']
    fields = ['first_name', 'last_name', 'email', 'inactive']

