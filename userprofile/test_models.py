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
    def setUpTestData(self):
        user = User.objects.create_user(
            username="testuser", password="password", email="test@test.com"
        )
        UserProfile.objects.create(full_name='John Joe', user=user)

    def test_create_profile(self):
        
        self.assertEqual(str(name), 'John Joe')
