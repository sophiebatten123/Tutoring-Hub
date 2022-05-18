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
        fields = (
            'full_name', 'year_group', 'about_me',
            'maths', 'english', 'science',
            )
        labels = {
            "maths": "<br /> How do you find the following subjects? What\
                 would you like to work on in lessons? <br /><br />Maths:",
            "english": "English: ",
            "science": "Science: ",
            "about_me": "<br /> Tell us about yourself: ",
        }
