'''
Importing the relevant packages.
'''
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json


def tutor_one(request):
    '''
    This renders the first tutor page.
    '''
    return render(request, 'tutorprofile/tutor_one.html')


def tutor_two(request):
    '''
    This renders the second tutor page.
    '''
    return render(request, 'tutorprofile/tutor_two.html')


def tutor_three(request):
    '''
    This renders the third tutor page.
    '''
    return render(request, 'tutorprofile/tutor_three.html')


@login_required
def confirm_booking(request):
    '''
    This allows the student to book in a lesson with the
    tutor. It sends data to the users database which
    will then be viewable on thier profile page
    '''

    if request.method == 'POST':
        request_body = json.loads(request.body)
        date = request_body['date']
        time = request_body['time']

    print(request.POST[date, time])
    return HttpResponse('hello')
