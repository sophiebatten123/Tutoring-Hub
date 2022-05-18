'''
Importing the relevant packages.
'''
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

YEAR_GROUPS = (
    ('9', 'Year 9'),
    ('10', 'Year 10'),
    ('11', 'Year 11'),
)


class UserProfile(models.Model):
    '''
    Creates the user profile information for students & tutors.
    Some of this information will be displayed upon their
    profile pages.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    maths = models.CharField(max_length=200, null=True, blank=True)
    english = models.CharField(max_length=200, null=True, blank=True)
    science = models.CharField(max_length=200, null=True, blank=True)
    year_group = models.CharField(
        max_length=13, choices=YEAR_GROUPS, default='9'
    )
    about_me = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        '''
        Override the original save method
        '''
        if not self.slug:
            self.slug = self.user
        super().save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_or_update_user_profile(instance, created):
    '''
    Create or update the user profile
    '''
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users save the information
    instance.userprofile.save()
