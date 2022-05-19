'''
Unit testing for models
'''
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Review


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

    def test_user_has_review(self):
        '''
        Test to check that the student can create a review and that it returns
        the correct string.
        '''
        self.assertEquals(Review.objects.all().count(), 1)
        self.assertEquals(str(self.review), 'test_name created a post')
