# pylint: disable=locally-disabled, no-member
'''
Unit testing for models
'''
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Review, Booking


class TestModels(TestCase):
    '''
    Testing the models file
    '''
    def setUp(self):
        '''
        Sets up the variables ready for testing
        '''
        self.user1 = User.objects.create(
            username="test_name",
            password="password12345367",
            email="test@test.com",
        )
        self.review = Review.objects.create(
            student=self.user1,
            review='test_review',
        )
        self.booking1 = Booking.objects.create(
            student=self.user1,
            time='test_time',
            date='test_date',
            tutor='test_tutor',
        )

    def test_user_has_review(self):
        '''
        Test to check that the student can create a review and that it returns
        the correct string.
        '''
        self.assertEqual(Review.objects.all().count(), 1)
        self.assertEqual(str(self.review), 'test_name created a post')

    def test_user_has_booking(self):
        '''
        Test to check that the student can book in a lesson with a tutor.
        '''
        self.assertEqual(Booking.objects.all().count(), 1)
        self.assertEqual(
            str(self.booking1),
            'test_name on test_date test_time with test_tutor'
        )
