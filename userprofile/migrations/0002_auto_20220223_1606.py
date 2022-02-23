# Generated by Django 3.2 on 2022-02-23 16:06

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('year_group', models.CharField(choices=[('year_7', 'Year 7'), ('year_8', 'Year 8'), ('year_9', 'Year 9'), ('year_10', 'Year 10'), ('year_11', 'Year 11')], default='year_7', max_length=7)),
                ('about_me', models.TextField()),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_page', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]