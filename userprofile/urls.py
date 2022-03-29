'''
Importing the relevant packages.
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('delete_booking/', views.delete_booking, name='delete_booking')
]
