# Generated by Django 3.2 on 2022-04-11 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorprofile', '0010_alter_review_tutor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='tutor',
            field=models.CharField(max_length=50),
        ),
    ]
