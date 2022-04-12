from django.contrib import admin
from .models import UserProfile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(UserProfile)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('full_name', 'slug', 'year_group',)
    search_fields = ['full_name', 'year_group']
    prepopulated_fields = {'slug': ('full_name',)}
    summernote_fields = ('about_me', 'maths', 'english', 'science',)
    actions = ['approve_profile']

    def approve_profile(self, request, queryset):
        queryset.update(approve=True)
