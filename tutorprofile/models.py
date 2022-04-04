'''
Imports the relevant packages
'''
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Booking(models.Model):
    '''
    Booking model
    '''
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    tutor = models.CharField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    student = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} booked a lesson on {self.date} at {self.time} with {self.tutor}"
