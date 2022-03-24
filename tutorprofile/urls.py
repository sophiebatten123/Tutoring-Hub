'''
Importing the relevant packages.
'''
from django.urls import path
from . import views

urlpatterns = [
    path('tutor_one/', views.tutor_one, name='tutor_one'),
    path('tutor_two/', views.tutor_two, name='tutor_two'),
    path('tutor_three/', views.tutor_three, name='tutor_three'),
    path('tutor_one/confirm_booking/', views.confirm_booking, name='confirm_booking'),
]