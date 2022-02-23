from .models import Profile
from django import forms


class MakeProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields =('full_name', 'year_group', 'about_me', 'featured_image')