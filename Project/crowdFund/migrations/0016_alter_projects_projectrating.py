# Generated by Django 4.0.5 on 2022-07-03 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdFund', '0015_projects_numberofusersrated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='projectRating',
            field=models.IntegerField(default=0),
        ),
    ]
