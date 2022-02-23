# Generated by Django 3.2 on 2022-02-23 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20220223_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year_group',
            field=models.CharField(choices=[('year_7', 'Year 7'), ('year_8', 'Year 8'), ('year_9', 'Year 9'), ('year_10', 'Year 10'), ('year_11', 'Year 11'), ('tutor_account', '')], default='year_7', max_length=13),
        ),
    ]
