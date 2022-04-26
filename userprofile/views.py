'''
Importing the relevant packages.
'''
import json
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from tutorprofile.models import Booking
from .models import UserProfile
from .forms import MakeProfileForm


@login_required
def profile(request):
    ''' This will render the profile template '''
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = MakeProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated')
        else:
            messages.error(request, 'Update failed. Ensure your data is valid')

    else:
        form = MakeProfileForm(instance=user_profile)
        print(user_profile)

    template = 'userprofile/profile.html'
    context = {
        'profile': user_profile,
        'form': form,
        'on_profile_page': True
    }

    return render(request, template, context)


def delete_booking(request):
    '''
    This will delete the users booking
    '''
    request_body = json.loads(request.body)
    student_id = request_body['id']

    if Booking.objects.filter(student=request.user).exists():
        Booking.objects.filter(id=student_id).delete()
        messages.success(request, ('Tutoring session deleted'))
        return HttpResponse(status=201)
    else:
        print('nothing')

    context = {
        'profile_delete': 'Your profile is deleted',
    }

    return render(request, 'userprofile/upcoming_lessons.html', context)


def upcoming_lessons(request):
    '''
    Renders the students upcoming lessons
    '''
    template = 'userprofile/upcoming_lessons.html'
    context = {
        'bookings': Booking.objects.filter(student=request.user),
    }

    return render(request, template, context)
