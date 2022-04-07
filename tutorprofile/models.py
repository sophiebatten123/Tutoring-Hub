'''
Imports the relevant packages
'''
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


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


class Review(models.Model):
    '''
    Creating a tutor review
    '''
    tutor = models.CharField(max_length=50)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    review = models.CharField(max_length=150)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.review
