'''
Importing the relevant packages.
'''
from django.shortcuts import render


def home(request):
    '''
    This renders the home page.
    '''
    return render(request, 'home/index.html')
