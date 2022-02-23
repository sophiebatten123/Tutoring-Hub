from django.db import models
from django.contrib.auth.models import User
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

class Profile(models.Model):
    full_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="profile_page"
    )
    year_group = models.CharField(max_length=13, choices=YEAR_GROUPS, default='year_7')
    about_me = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    account_type = models.CharField(max_length=7, choices=ACCOUNT_TYPE, default='student')
    status = models.IntegerField(choices=STATUS, default=0)

    def _str_(self):
        return self.full_name
