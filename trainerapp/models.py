from django.db import models
from django.urls import reverse
from datetime import time


class Attendee(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    attended = models.BooleanField(default=False)


class Course(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    hours = models.DecimalField(decimal_places=1, max_digits=3)
    inactive = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', args=[str(self.id)])


class Event(models.Model):

    time_choices = (
        (time(7, 0, 0), '07:00'),
        (time(7, 30, 0), '07:30'),
        (time(8, 0, 0), '08:00'),
        (time(8, 30, 0), '08:30'),
        (time(9, 0, 0), '09:00'),
        (time(9, 30, 0), '09:30'),
        (time(10, 0, 0), '10:00'),
        (time(10, 30, 0), '10:30'),
        (time(11, 0, 0), '11:00'),
        (time(11, 30, 0), '11:30'),
        (time(12, 0, 0), '12:00'),
        (time(12, 30, 0), '12:30'),
        (time(13, 0, 0), '13:00'),
        (time(13, 30, 0), '13:30'),
        (time(14, 0, 0), '14:00'),
        (time(14, 30, 0), '14:30'),
        (time(15, 0, 0), '15:00'),
        (time(15, 30, 0), '15:30'),
        (time(16, 0, 0), '16:00'),
        (time(16, 30, 0), '16:30'),
        (time(17, 0, 0), '17:00'),
    )

    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    start_date = models.DateField()
    start_time = models.TimeField(choices=time_choices)
    end_date = models.DateField()
    end_time = models.TimeField(choices=time_choices)
    location = models.CharField(max_length=128, blank=True)
    capacity = models.IntegerField(blank=True)

    def __str__(self):
        return "".join([str(self.course), ': ',
                        self.start_date.strftime('%B %#d, %Y'), ' ',
                        self.start_time.strftime('%#I%p')])

    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])


class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    inactive = models.BooleanField(blank=True)

    class Meta:
        ordering = ('last_name', 'first_name')

    def get_absolute_url(self):
        return reverse('student_detail', args=[str(self.id)])

    def __str__(self):
        return "".join([self.last_name, ', ', self.first_name])
