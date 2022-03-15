'''
Importing the relevant packages.
'''
from django.shortcuts import render


def tutor_one(request):
    return render(request, 'tutorprofile/tutor_one.html')


def tutor_two(request):
    return render(request, 'tutorprofile/tutor_two.html')


def tutor_three(request):
    return render(request, 'tutorprofile/tutor_three.html')