from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crowdFund.models import *
from django.forms import ModelForm


class LoginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserProfiles
        fields = (
            'username',
            'password',
        )


class RegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = models.EmailField(blank=True)

    class Meta:
        model = UserProfiles
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'profile_pic',
            'phone_number',
        )


class CreateProjectForm(ModelForm):
    class Meta:
        model = projects
        fields = (
            'title',
            'category',
            'target',
            'endTime',
            'Details',
        )


class imagesForm(ModelForm):
    class Meta:
        model = images
        fields = (
            'title',
        )


class TagsForm(ModelForm):
    class Meta:
        model = Tags
        fields = (
            'title',
        )


class EditForm(ModelForm):
    class Meta:
        model = UserProfiles
        fields = (
            'first_name',
            'last_name',
            'profile_pic',
            'phone_number',
            'b_date',
            'facebook_profile',
            'country',
        )
