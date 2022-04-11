'''
Importing the relevant packages.
'''
from django.urls import path
from . import views


urlpatterns = [
    path('tutor_one/', views.tutor_one, name='tutor_one'),
    path('tutor_one/confirm_booking/', views.confirm_booking, name='confirm_booking'),
    path('tutor_one/confirm_booking/success/', views.confirm_booking, name='confirm_booking_success'),
    path('tutor_one/reviews/', views.ReviewListTutorOne.as_view(), name='tutor_one_reviews'),
    path('tutor_one/profile/', views.tutor_one_profile, name='tutor_one_profile'),
    path('tutor_one/qualifications/', views.tutor_one_qualifications, name='tutor_one_qualifications'),
    path('tutor_two/', views.tutor_two, name='tutor_two'),
    path('tutor_two/confirm_booking/', views.confirm_booking, name='confirm_booking'),
    path('tutor_two/confirm_booking/success/', views.confirm_booking, name='confirm_booking_success'),
    path('tutor_two/reviews/', views.ReviewListTutorTwo.as_view(), name='tutor_two_reviews'),
    path('tutor_two/profile/', views.tutor_two_profile, name='tutor_two_profile'),
    path('tutor_two/qualifications/', views.tutor_two_qualifications, name='tutor_two_qualifications'),
    path('tutor_three/', views.tutor_three, name='tutor_three'),
    path('tutor_three/confirm_booking/', views.confirm_booking, name='confirm_booking'),
    path('tutor_three/confirm_booking/success/', views.confirm_booking, name='confirm_booking_success'),
    path('tutor_three/reviews/', views.ReviewListTutorThree.as_view(), name='tutor_three_reviews'),
    path('tutor_three/profile/', views.tutor_three_profile, name='tutor_three_profile'),
    path('tutor_three/qualifications/', views.tutor_three_qualifications, name='tutor_three_qualifications'),
]
