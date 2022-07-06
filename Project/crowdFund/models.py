from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import datetime
# Create your models here.
Categories = (
    ("c", "Charity"),
    ("p", "Personal"),
    ("t", "Team Project"),
)


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE, blank=True)
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=20, null=False)
    first_name = models.CharField(max_length=12, null=False)
    last_name = models.CharField(max_length=12, null=False)
    email = models.EmailField(null=False)
    Activation_Status = models.BooleanField()
    Activation_Link = models.URLField()
    b_date = models.DateField()
    phone_number = PhoneNumberField()
    profilePic = models.ImageField(
        upload_to='profileImages',)
    country = models.CharField(max_length=15,)
    facebook_profile = models.URLField()


class UserProfiles(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE, blank=True)
    username = models.CharField(max_length=20, null=False, unique=True)
    password = models.CharField(max_length=20, null=False)
    first_name = models.CharField(max_length=12, null=False)
    last_name = models.CharField(max_length=12, null=False)
    email = models.EmailField(null=False)
    Activation_Status = models.BooleanField(
        null=True, blank=True, default=False)
    Activation_Link = models.URLField(null=True, blank=True)
    b_date = models.DateField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    profile_pic = models.ImageField(
        upload_to='profileimage', blank=False)
    country = models.CharField(max_length=15,)
    facebook_profile = models.URLField(null=True, blank=True)
    Totaldonated = models.BigIntegerField(default=0)


class projects(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20, null=False, unique=True)
    createdByUsername = models.CharField(
        max_length=20, null=False)
    category = models.CharField(max_length=1, choices=Categories)
    Details = models.TextField(max_length=200, null=True, blank=True)
    target = models.BigIntegerField(null=False)
    startTime = models.DateField(
        null=False, default=datetime.date(datetime.now()))
    endTime = models.DateField(null=False)
    numberOfUsersRated = models.IntegerField(default=0)
    donations = models.BigIntegerField(default=0)
    projectRating = models.IntegerField(default=0)


class images(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.ImageField(
        upload_to='profileimage', blank=False)
    createdByProject = models.CharField(
        max_length=20, null=True, blank=True)


class Tags(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    ProjectTitle = models.CharField(
        max_length=20, null=True, blank=True, default="")
