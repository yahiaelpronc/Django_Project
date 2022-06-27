from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


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
    Activation_Status = models.BooleanField(null=True, blank=True)
    Activation_Link = models.URLField(null=True, blank=True)
    b_date = models.DateField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    profile_pic = models.ImageField(
        null=True, blank=True)
    country = models.CharField(max_length=15,)
    facebook_profile = models.URLField(null=True, blank=True)
