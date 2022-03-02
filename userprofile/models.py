'''
Importing the relevant packages.
'''
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from cloudinary.models import CloudinaryField

YEAR_GROUPS = (
    ('year_7', 'Year 7'),
    ('year_8', 'Year 8'),
    ('year_9', 'Year 9'),
    ('year_10', 'Year 10'),
    ('year_11', 'Year 11'),
    ('tutor_account', ''),
)

ACCOUNT_TYPE = (
    ('student', 'Student'),
    ('tutor', 'Tutor'),
)

STATUS = ((0, "Draft"), (1, "Published"))


class UserProfile(models.Model):
    '''
    Creates the user profile information for students & tutors.
    Some of this information will be displayed upon their
    profile pages.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    year_group = models.CharField(max_length=13, choices=YEAR_GROUPS, default='year_7')
    about_me = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    account_type = models.CharField(max_length=7, choices=ACCOUNT_TYPE, default='student')
    status = models.IntegerField(choices=STATUS, default=0)

    def save(self, *args, **kwargs):
        '''
        Override the original save method
        '''
        if not self.slug:
            self.slug = self.user.username
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

  
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    '''
    Create or update the user profile
    '''
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users save the information
    instance.userprofile.save()
