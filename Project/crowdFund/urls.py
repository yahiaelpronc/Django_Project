"""demo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls import include
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', home),
    path('login', loginUserView),
    path('logout', LogoutView.as_view(template_name='logout.html')),
    path('Register', CreateUserView, name='register'),
    path('profile', profile, name='profile'),
    path('editprofile', editprofile, name='editprofile'),
    path('deleteprofile', deleteprofile, name='deleteprofile'),
    path('createProject', createProject, name='createProject'),
    path('myProjects', myProjects, name='myProjects'),
    path('allProjects', allProjects, name='allProjects'),
    path('viewprojectInvalid', viewprojectInvalid, name='viewprojectInvalid'),
    path('viewProjects', viewProjects, name='projects'),
    path('viewProjects/<projectTitle>', viewProjects, name='projects'),
    path('donateProject/<title>',
         donateProject, name='donateProject'),
    path('rateProject/<title>/<int:val>', rateProject, name='rateProject'),
    path('reportProject/<title>', reportProject, name='reportProject'),
    path('cancelProject/<title>', cancelProject, name='cancelProject'),
    path('addimages', addimages, name='addimages'),
    path('addtags', addtags, name='addtags'),
    path('search',search, name='search'),
    path('verify/<str:username>/<dates>', verify, name='verify'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
