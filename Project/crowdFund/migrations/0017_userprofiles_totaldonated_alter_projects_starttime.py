# Generated by Django 4.0.5 on 2022-07-06 22:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdFund', '0016_alter_projects_projectrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='Totaldonated',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='projects',
            name='startTime',
            field=models.DateField(default=datetime.date(2022, 7, 7)),
        ),
    ]
