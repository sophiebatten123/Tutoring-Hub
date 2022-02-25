from django.shortcuts import render, get_object_or_404
from .forms import MakeProfile
from .models import Profile
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):

    profile = get_object_or_404(Profile, author=request.author)

    if request.method == 'POST':
        # create a new instance of the user profile form using post data
        form = MakeProfile(request.POST, instance=profile)
        # checks that the form is valid
        if form.is_valid():
            # valid = save and send a success message
            form.save()
            messages.success(request, 'Profile updated sucessfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = Profile(instance=profile)

    return render(
        request,
        'userprofile/profile.html',
        {
            'profile': profile,
            'form': MakeProfile(),
        },
    )
