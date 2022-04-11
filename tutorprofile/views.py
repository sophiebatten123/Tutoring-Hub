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


def tutor_one_profile(request):
    return render(request, 'tutorprofile/tutor_one_profile.html')


def tutor_one_qualifications(request):
    return render(request, 'tutorprofile/tutor_one_qualifications.html')


def tutor_two(request):
    '''
    This renders the second tutor page.
    '''
    tutor_two_bookings = Booking.objects.filter(tutor='Jennifer Roberts')

    context = {
        'tutor_two_bookings': tutor_two_bookings,
    }

    return render(request, 'tutorprofile/tutor_two.html', context)


def tutor_two_profile(request):
    return render(request, 'tutorprofile/tutor_two_profile.html')


def tutor_two_qualifications(request):
    return render(request, 'tutorprofile/tutor_two_qualifications.html')


def tutor_three(request):
    '''
    This renders the third tutor page.
    '''
    tutor_three_bookings = Booking.objects.filter(tutor='Mark Macintosh')

    context = {
        'tutor_three_bookings': tutor_three_bookings,
    }
    return render(request, 'tutorprofile/tutor_three.html', context)


def tutor_three_profile(request):
    return render(request, 'tutorprofile/tutor_three_profile.html')


def tutor_three_qualifications(request):
    return render(request, 'tutorprofile/tutor_three_qualifications.html')
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


class ReviewListTutorOne(generic.ListView):
    '''
    Allows the student to rate the tutor
    '''
    model = Review
    queryset = Review.objects.filter(Q(status=1) & Q(tutor='Barry Hyman')).order_by('-created_on')
    template_name = 'tutorprofile/tutor_one_reviews.html'


class ReviewListTutorTwo(generic.ListView):
    '''
    Allows the student to rate the tutor
    '''
    model = Review
    queryset = Review.objects.filter(Q(status=1) & Q(tutor='Jennifer Roberts')).order_by('-created_on')
    template_name = 'tutorprofile/tutor_two_reviews.html'


class ReviewListTutorThree(generic.ListView):
    '''
    Allows the student to rate the tutor
    '''
    model = Review
    queryset = Review.objects.filter(Q(status=1) & Q(tutor='Mark Macintosh')).order_by('-created_on')
    template_name = 'tutorprofile/tutor_three_reviews.html'