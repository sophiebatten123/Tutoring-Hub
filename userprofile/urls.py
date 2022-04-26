'''
Importing the relevant packages.
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('upcoming_lessons/', views.upcoming_lessons, name='upcoming_lessons'),
    path('upcoming_lessons/delete_booking/', views.delete_booking, name='delete_booking')
]
