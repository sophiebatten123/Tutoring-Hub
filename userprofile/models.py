'''
Importing the relevant packages.
'''
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from cloudinary.models import CloudinaryField

YEAR_GROUPS = (
    ('9', 'Year 9'),
    ('10', 'Year 10'),
    ('11', 'Year 11'),
)

ACCOUNT_TYPE = (
    ('student', 'Student'),
    ('tutor', 'Tutor'),
)

GRADES = (
    ('1', 'Grade 1'),
    ('2', 'Grade 2'),
    ('3', 'Grade 3'),
    ('4', 'Grade 4'),
    ('5', 'Grade 5'),
    ('6', 'Grade 6'),
    ('7', 'Grade 7'),
    ('8', 'Grade 8'),
    ('9', 'Grade 9'),
)

SCIENCE = (
    ('cell-biology', 'Cell Biology'),
    ('infection-response', 'Infection and Response'),
)

class UserProfile(models.Model):
    '''
    Creates the user profile information for students & tutors.
    Some of this information will be displayed upon their
    profile pages.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    year_group = models.CharField(max_length=13, choices=YEAR_GROUPS, default='9')
    email = models.EmailField(max_length=254, null=True, blank=True)
    current_grade = models.CharField(max_length=6, choices=GRADES, default='1', null=True)
    predicted_grade = models.CharField(max_length=6, choices=GRADES, default='1', null=True)
    about_me = models.TextField()
    science = models.CharField(max_length=40, choices=SCIENCE, default='cell-biology')
    account_type = models.CharField(max_length=7, choices=ACCOUNT_TYPE, default='student')
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')

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
