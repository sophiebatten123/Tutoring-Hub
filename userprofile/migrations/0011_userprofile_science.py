# Generated by Django 3.2 on 2022-03-30 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_userprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='science',
            field=models.CharField(choices=[('cell-biology', 'Cell Biology'), ('infection-response', 'Infection and Response')], default='cell-biology', max_length=40),
        ),
    ]
