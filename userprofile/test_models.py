'''
Unit testing for models
'''
from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile


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
        self.userprofile = UserProfile.objects.create(
            user=self.user1,
            full_name='test_name',
        )

    def test_user_has_profile(self):
        '''
        Test to check that the student can create a profile
        '''
        self.assertEqual(UserProfile.objects.all().count(), 1)
        self.assertEqual(str(self.userprofile), 'test_name')
