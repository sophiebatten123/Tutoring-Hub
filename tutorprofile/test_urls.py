'''
Unit testing for urls
'''
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from .views import (
    tutor_one,
    tutor_one_profile,
    tutor_one_qualifications,
    tutor_two,
    tutor_two_profile,
    tutor_two_qualifications,
    tutor_three,
    tutor_three_profile,
    tutor_three_qualifications,
    confirm_booking,
    tutor_one_create_review,
    tutor_two_create_review,
    tutor_three_create_review,
)


class TestUrls(SimpleTestCase):
    '''
    testing the URLS for the tutorprofile
    '''
    def test_tutor_one_url(self):
        '''
        testing tutor one url
        '''
        url = reverse('tutor_one')
        self.assertEqual(resolve(url).func, tutor_one)

    def test_tutor_one_profile_url(self):
        '''
        testing tutor one profile url
        '''
        url = reverse('tutor_one_profile')
        self.assertEqual(resolve(url).func, tutor_one_profile)

    def test_tutor_one_qualifications_url(self):
        '''
        testing tutor one qualifications url
        '''
        url = reverse('tutor_one_qualifications')
        self.assertEqual(resolve(url).func, tutor_one_qualifications)

    def test_tutor_two_url(self):
        '''
        testing tutor two url
        '''
        url = reverse('tutor_two')
        self.assertEqual(resolve(url).func, tutor_two)

    def test_tutor_two_profile_url(self):
        '''
        testing tutor two profile url
        '''
        url = reverse('tutor_two_profile')
        self.assertEqual(resolve(url).func, tutor_two_profile)

    def test_tutor_two_qualifications_url(self):
        '''
        testing tutor two qualifications url
        '''
        url = reverse('tutor_two_qualifications')
        self.assertEqual(resolve(url).func, tutor_two_qualifications)

    def test_tutor_three_url(self):
        '''
        testing tutor three url
        '''
        url = reverse('tutor_three')
        self.assertEqual(resolve(url).func, tutor_three)

    def test_tutor_three_profile_url(self):
        '''
        testing tutor three profile url
        '''
        url = reverse('tutor_three_profile')
        self.assertEqual(resolve(url).func, tutor_three_profile)

    def test_tutor_three_qualifications_url(self):
        '''
        testing tutor three qualifications url
        '''
        url = reverse('tutor_three_qualifications')
        self.assertEqual(resolve(url).func, tutor_three_qualifications)

    def test_confirm_booking(self):
        '''
        testing confirm booking url
        '''
        url = reverse('confirm_booking')
        self.assertEqual(resolve(url).func, confirm_booking)

    def tutor_one_create_review(self):
        '''
        testing create a review for tutor one url
        '''
        url = reverse('tutor_one_create_review')
        self.assertEqual(resolve(url).func, tutor_one_create_review)

    def tutor_two_create_review(self):
        '''
        testing create a review for tutor two url
        '''
        url = reverse('tutor_two_create_review')
        self.assertEqual(resolve(url).func, tutor_two_create_review)

    def tutor_three_create_review(self):
        '''
        testing create a review for tutor three url
        '''
        url = reverse('tutor_three_create_review')
        self.assertEqual(resolve(url).func, tutor_three_create_review)
