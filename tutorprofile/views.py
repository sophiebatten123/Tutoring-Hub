'''
Importing the relevant packages.
'''
import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.db.models import Q
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from .models import Booking, Review
from .forms import ReviewForm


def tutor_one(request):
    '''
    This renders the first tutors booking page.
    '''
    tutor_one_bookings = Booking.objects.filter(tutor='Barry Hyman')

    context = {
        'tutor_one_bookings': tutor_one_bookings,
    }

    return render(request, 'tutorprofile/tutor_one.html', context)


def tutor_one_profile(request):
    '''
    Renders the tutor one profile page.
    '''
    return render(request, 'tutorprofile/tutor_one_profile.html')


def tutor_one_qualifications(request):
    '''
    Renders the tutor one's qualifications page.
    '''
    return render(request, 'tutorprofile/tutor_one_qualifications.html')


def tutor_two(request):
    '''
    This renders the second tutors booking page.
    '''
    tutor_two_bookings = Booking.objects.filter(tutor='Jennifer Roberts')

    context = {
        'tutor_two_bookings': tutor_two_bookings,
    }

    return render(request, 'tutorprofile/tutor_two.html', context)


def tutor_two_profile(request):
    '''
    Renders the tutor two's profile page.
    '''
    return render(request, 'tutorprofile/tutor_two_profile.html')


def tutor_two_qualifications(request):
    '''
    Renders the tutor two's qualifications page.
    '''
    return render(request, 'tutorprofile/tutor_two_qualifications.html')


def tutor_three(request):
    '''
    This renders the third tutors booking page.
    '''
    tutor_three_bookings = Booking.objects.filter(tutor='Mark Macintosh')

    context = {
        'tutor_three_bookings': tutor_three_bookings,
    }
    return render(request, 'tutorprofile/tutor_three.html', context)


def tutor_three_profile(request):
    '''
    Renders the tutor three's profile page.
    '''
    return render(request, 'tutorprofile/tutor_three_profile.html')


def tutor_three_qualifications(request):
    '''
    Renders the tutor three's qualifications page.
    '''
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
    queryset = Review.objects.filter(Q(tutor='Barry Hyman')).order_by('-created_on')
    template_name = 'tutorprofile/tutor_one_reviews.html'
    paginate_by = 6


class ReviewListTutorTwo(generic.ListView):
    '''
    Allows the student to rate the tutor
    '''
    model = Review
    queryset = Review.objects.filter(Q(tutor='Jennifer Roberts')).order_by('-created_on')
    template_name = 'tutorprofile/tutor_two_reviews.html'
    paginate_by = 6


class ReviewListTutorThree(generic.ListView):
    '''
    Allows the student to rate the tutor
    '''
    model = Review
    queryset = Review.objects.filter(Q(tutor='Mark Macintosh')).order_by('-created_on')
    template_name = 'tutorprofile/tutor_three_reviews.html'
    paginate_by = 6


@login_required
def tutor_one_create_review(request):
    '''
    Creating the tutor one review
    '''
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_form = form.save(commit=False)
            review_form.tutor = 'Barry Hyman'
            review_form.student = request.user
            review_form.save()
            messages.success(request, ('Thank you for your review!'))
            return HttpResponseRedirect('../reviews')
    else:
        form = ReviewForm()

    return render(request, 'tutorprofile/tutor_one_create_review.html', {'form': form})


@login_required
def tutor_two_create_review(request):
    '''
    Creating the tutor two review
    '''
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_form = form.save(commit=False)
            review_form.tutor = 'Jennifer Roberts'
            review_form.student = request.user
            review_form.save()
            messages.success(request, ('Thank you for your review!'))
            return HttpResponseRedirect('../reviews')
    else:
        form = ReviewForm()

    return render(request, 'tutorprofile/tutor_two_create_review.html', {'form': form})


@login_required
def tutor_three_create_review(request):
    '''
    Creating the tutor two review
    '''
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_form = form.save(commit=False)
            review_form.tutor = 'Mark Macintosh'
            review_form.student = request.user
            review_form.save()
            messages.success(request, ('Thank you for your review!'))
            return HttpResponseRedirect('../reviews')
    else:
        form = ReviewForm()

    return render(request, 'tutorprofile/tutor_three_create_review.html', {'form': form})
