from .models import Review
from django.forms import ModelForm
from django import forms


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('review', 'tutor',)
