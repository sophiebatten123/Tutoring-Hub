'''
Importing the relevant packages.
'''
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .forms import MakeProfileForm
from .models import UserProfile


@login_required
def profile(request):
    ''' This will render the profile template '''
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = MakeProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated')
        else:
            messages.error(request, ('Update failed. Ensure your data is valid'))

    else:
        form = MakeProfileForm(instance=profile)

    template = 'userprofile/profile.html'
    context = {
        'form': form,
        'on_profile_page': True
    }
   
    return render(request, template, context)
