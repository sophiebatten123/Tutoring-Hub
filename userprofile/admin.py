from django.contrib import admin
from .models import UserProfile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(UserProfile)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('full_name', 'slug', 'year_group', 'account_type')
    search_fields = ['full_name', 'year_group', 'account_type']
    prepopulated_fields = {'slug': ('full_name',)}
    list_filter = ('account_type',)
    summernote_fields = ('about_me')
    actions = ['approve_profile']

    def approve_profile(self, request, queryset):
        queryset.update(approve=True)
