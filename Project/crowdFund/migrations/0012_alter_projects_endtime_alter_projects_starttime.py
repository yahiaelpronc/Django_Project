# Generated by Django 4.0.5 on 2022-07-03 17:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdFund', '0011_alter_projects_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='endTime',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='projects',
            name='startTime',
            field=models.DateField(default=datetime.date(2022, 7, 3)),
        ),
    ]