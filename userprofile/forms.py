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
        fields = ('full_name', 'year_group', 'about_me', 'featured_image',)

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'year_group': forms.TextInput(attrs={'class': 'form-control'}),
            'about_me': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_image': forms.TextInput(attrs={'class': 'form-control'}),
        }
