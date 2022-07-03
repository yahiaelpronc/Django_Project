# Generated by Django 4.0.5 on 2022-07-03 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdFund', '0010_alter_projects_starttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='category',
            field=models.CharField(choices=[('c', 'Charity'), ('p', 'Personal'), ('t', 'Team Project')], default='c', max_length=1),
            preserve_default=False,
        ),
    ]
