# Generated by Django 4.0.5 on 2022-07-03 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdFund', '0014_alter_tags_projecttitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='numberOfUsersRated',
            field=models.IntegerField(default=0),
        ),
    ]
