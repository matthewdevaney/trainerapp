from django.db import models


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


class Event(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    location = models.CharField(max_length=128, blank=True)
    capacity = models.IntegerField(blank=True)

    def __str__(self):
        return "".join([str(self.course), ': ', self.start_datetime.strftime('%B %#d, %Y @ %#I%p')])

class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    inactive = models.BooleanField(blank=True)

    def __str__(self):
        return "".join([self.last_name, ', ', self.first_name])
