'''
Importing the relevant packages.
'''
import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.db.models import Q
from django.contrib import messages
from django.http import JsonResponse
from .models import Booking, Review


def tutor_one(request):
    '''
    This renders the first tutor page.
    '''
    tutor_one_bookings = Booking.objects.filter(tutor='Barry Hyman')

    context = {
        'tutor_one_bookings': tutor_one_bookings,
    }

    return render(request, 'tutorprofile/tutor_one.html', context)


def tutor_two(request):
    '''
    This renders the second tutor page.
    '''
    tutor_two_bookings = Booking.objects.filter(tutor='Jennifer Roberts')

    context = {
        'tutor_two_bookings': tutor_two_bookings,
    }

    return render(request, 'tutorprofile/tutor_two.html', context)


def tutor_three(request):
    '''
    This renders the third tutor page.
    '''
    tutor_three_bookings = Booking.objects.filter(tutor='Mark Macintosh')

    context = {
        'tutor_three_bookings': tutor_three_bookings,
    }
    return render(request, 'tutorprofile/tutor_three.html', context)


@login_required
def confirm_booking(request):
    '''
    This allows the student to book in a lesson with the
    tutor. It sends data to the users database which
    will then be viewable on thier profile page
    '''

    if request.method == 'POST':

        booking = Booking()

        request_body = json.loads(request.body)
        date = request_body['date']
        time = request_body['time']
        tutor = request_body['tutor']
        subject = request_body['subject']

        if Booking.objects.filter(Q(student=request.user) & Q(tutor=tutor)).exists():
            messages.success(request, ('You can only have one lesson booked per tutor each week.'))
        else:
            booking.date = date
            booking.time = time
            booking.tutor = tutor
            booking.subject = subject
            booking.student = request.user
            booking.save()
            messages.success(request, ('You have booked in the lesson!'))

        bookings = Booking.objects.all().values()

        template_name = "userprofile/profile.html"

        args = {
            "bookings": list(bookings),
        }
        return JsonResponse(args)

    return render(request, template_name, args)
