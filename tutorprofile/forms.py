'''
Imports the relevant packages
'''
from django.forms import ModelForm
from .models import Review


class ReviewForm(ModelForm):
    '''
    Creates the review tutor form fields.
    '''
    class Meta:
        '''
        Specifies the model and fields that are displayed on the form.
        '''
        model = Review
        fields = ('review',)
