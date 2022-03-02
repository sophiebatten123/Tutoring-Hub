'''
Importing the relevant packages.
'''
from django import forms
from .models import UserProfile


class MakeProfileForm(forms.ModelForm):
    '''
    This is the information which is included on the profile sign up page.
    '''
    class Meta:
        '''
        Featured fields in the sign up.
        '''
        model = UserProfile
        fields = ('full_name', 'about_me', 'year_group',)
