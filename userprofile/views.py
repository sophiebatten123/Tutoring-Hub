'''
Importing the relevant packages.
'''
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import MakeProfileForm
from tutorprofile.models import Booking
import json

@login_required
def profile(request):
    ''' This will render the profile template '''
    user_profile = get_object_or_404(UserProfile, user=request.user)
    print(user_profile)
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
        'bookings': Booking.objects.filter(student=request.user),
        'form': form,
        'on_profile_page': True
    }

    return render(request, template, context)


def delete_booking(request):
    '''
    This will delete the users booking
    '''
    request_body = json.loads(request.body)
    id = request_body['id']

    print(id)

    Booking.objects.filter(id=id).delete()

    context = {
        'profile_delete': 'Your profile is deleted',
    }

    return render(request, 'userprofile/profile.html', context)
