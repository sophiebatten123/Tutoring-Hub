'''
Imports the relevant packages
'''
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Booking, Review

# Register your models here.


@admin.register(Review)
class PostReview(SummernoteModelAdmin):
    '''
    Posts the review form onto the tutor profiles.
    '''
    list_display = ('student', 'tutor', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['student', 'tutor']
    summernote_fields = ('review')


@admin.register(Booking)
class PostBooking(admin.ModelAdmin):
    '''
    Posts the booking form onto the tutor profiles.
    '''
    list_display = ('student', 'date', 'time')
    search_fields = ['student', 'date', 'time']

    def approve_booking(self, queryset):
        '''
        Approves the booking.
        '''
        queryset.update(approve=True)
