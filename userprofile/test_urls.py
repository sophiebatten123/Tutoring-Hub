'''
Unit testing for urls
'''
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from .views import (
    profile,
    delete_booking,
)


class TestUrls(SimpleTestCase):
    '''
    testing the URLS for the userprofile
    '''
    def profile(self):
        '''
        testing profile url
        '''
        url = reverse('profile')
        self.assertEqual(resolve(url).func, profile)

    def delete_booking(self):
        '''
        testing delete_booking url
        '''
        url = reverse('delete_booking')
        self.assertEqual(resolve(url).func, delete_booking)
