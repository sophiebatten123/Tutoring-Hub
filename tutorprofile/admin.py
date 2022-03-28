from django.contrib import admin
from .models import Booking

# Register your models here.


@admin.register(Booking)
class PostBooking(admin.ModelAdmin):
    list_display = ('student', 'date', 'time')
    search_fields = ['student', 'date', 'time']

    def approve_booking(self, request, queryset):
        queryset.update(approve=True)