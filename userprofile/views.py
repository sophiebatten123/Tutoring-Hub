'''
Importing the relevant packages.
'''
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import MakeProfileForm


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
            messages.error(request, ('Update failed. Ensure your data is valid'))

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
