'''
Importing the relevant packages.
'''
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import UserProfile


@admin.register(UserProfile)
class PostAdmin(SummernoteModelAdmin):
    '''
    Generates the profile form on the users page.
    '''
    list_display = ('full_name', 'slug', 'year_group',)
    search_fields = ['full_name', 'year_group']
    prepopulated_fields = {'slug': ('full_name',)}
    summernote_fields = ('about_me', 'maths', 'english', 'science',)
    actions = ['approve_profile']

    def approve_profile(self, queryset):
        '''
        Approves the users profile.
        '''
        queryset.update(approve=True)
