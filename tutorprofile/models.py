'''
Imports the relevant packages
'''
from django.db import models
from userprofile.models import UserProfile

# Create your models here.

class Booking(models.Model):
    '''
    Booking model
    '''
    date = models.DateField()
    time = models.TimeField()
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
