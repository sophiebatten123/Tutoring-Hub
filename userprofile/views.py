from django.shortcuts import render
from .forms import MakeProfile

def profile(request):
    return render(
        request,
        'userprofile/profile.html',
        {
            "make_profile": MakeProfile()
        },
    )

