from .models import Profile
from django import forms


class MakeProfile(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('full_name', 'year_group', 'about_me', 'featured_image',)
    
    widgets = {
        'full_name': forms.TextInput(attrs={'class': 'form-control'}),
        'year_group': forms.TextInput(attrs={'class': 'form-control'}),
        'about_me': forms.TextInput(attrs={'class': 'form-control'}),
        'featured_image': forms.TextInput(attrs={'class': 'form-control'}),
    }
