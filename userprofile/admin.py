from django.contrib import admin
from .models import Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Profile)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('about_me')
