# Generated by Django 3.2 on 2022-04-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorprofile', '0013_remove_review_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]
