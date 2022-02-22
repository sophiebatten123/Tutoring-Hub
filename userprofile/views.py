from django.shortcuts import render

def profile(request):
    return render(request, 'userprofile/profile.html')
