from django.contrib import admin
from .models import Booking, Review
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Review)
class PostReview(SummernoteModelAdmin):

    list_display = ('student', 'tutor', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['student', 'tutor']
    summernote_fields = ('review')


@admin.register(Booking)
class PostBooking(admin.ModelAdmin):
    list_display = ('student', 'date', 'time')
    search_fields = ['student', 'date', 'time']

    def approve_booking(self, request, queryset):
        queryset.update(approve=True)