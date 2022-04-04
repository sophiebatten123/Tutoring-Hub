'''
Importing the relevant packages.
'''
from django.urls import path
from . import views

urlpatterns = [
    path('tutor_one/', views.tutor_one, name='tutor_one'),
    path('tutor_two/', views.tutor_two, name='tutor_two'),
    path('tutor_three/', views.tutor_three, name='tutor_three'),
    path('tutor_one/check_booking/', views.check_booking, name='check_booking'),
    path('tutor_two/check_booking/', views.check_booking, name='check_booking'),
    path('tutor_three/check_booking/', views.check_booking, name='check_booking'),
    path('tutor_one/confirm_booking/', views.confirm_booking, name='confirm_booking'),
    path('tutor_two/confirm_booking/', views.confirm_booking, name='confirm_booking'),
    path('tutor_three/confirm_booking/', views.confirm_booking, name='confirm_booking'),
    path('tutor_one/confirm_booking/success/', views.confirm_booking, name='confirm_booking_success'),
    path('tutor_two/confirm_booking/success/', views.confirm_booking, name='confirm_booking_success'),
    path('tutor_three/confirm_booking/success/', views.confirm_booking, name='confirm_booking_success'),
]