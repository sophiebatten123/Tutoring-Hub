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
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    student = models.ForeignKey(UserProfile, default=None, on_delete=models.CASCADE)
