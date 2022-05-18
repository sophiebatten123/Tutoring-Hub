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
        self.user = User.objects.create(
            username="testuser", password="password", email="test@test.com"
        )

    def test_profile_model(self, user):
        '''
        Testing that the user profiles string is returned correctly
        '''
        name = UserProfile.objects.create(user=user)
        self.assertEqual(str(name), user)
