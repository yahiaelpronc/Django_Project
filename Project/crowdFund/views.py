from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.views import View
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from .models import UserProfiles
from .forms import *
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

import json

# Create your views here.


def home(request):
    if (request.session.get('username') != None):
        return render(request, 'index.html')
    else:
        return HttpResponseRedirect('user/logout')


def loginUserView(request):
    if(request.method == 'GET'):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        user = UserProfiles.objects.filter(
            username=request.POST['username'], password=request.POST['password'])
        if(len(user) != 0):
            user = UserProfiles.objects.get(username=request.POST['username'])
            request.session['username'] = user.username
            request.session['profile_pic_url'] = user.profile_pic.url
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            request.session['email'] = user.email
            request.session['b_date'] = user.b_date
            p = str(user.phone_number)
            request.session['phone_number'] = p
            request.session['country'] = user.country
            request.session['facebook_profile'] = user.facebook_profile
            return HttpResponseRedirect("/")
        else:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})


def CreateUserView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {}
            context['user'] = UserProfiles.objects.get(
                username=request.POST['username'])
            return render(request, 'login.html', context)
        else:
            form = RegistrationForm(request.POST)
            for field in form:
                print("Field Error:", field.name,  field.errors)
            return HttpResponse(form.errors)
    else:
        form = RegistrationForm()
        return render(request, 'Registration.html', {'form': form})


def profile(request):
    if (request.session.get('username') != None):
        return render(request, 'profile_info.html')
    else:
        return HttpResponseRedirect('logout')


def editprofile(request):
    if (request.session.get('username') != None):
        if request.method == 'POST':
            form = EditForm(request.POST, request.FILES)
            if form.is_valid():

                # user = UserProfiles.objects.get(id=request.POST['tid'])
                # user.profile_pic.url = form.cleaned_data['profile_pic'].url
                # user.first_name
                # user.last_name
                # user.email
                # user.b_date
                # p = str(user.phone_number)
                # p
                # user.country
                # user.facebook_profile
                user = UserProfiles.objects.get(
                    username=request.session['username'])
                form = EditForm(request.POST, request.FILES, instance=user)
                # Set New Session Vars
                request.session['profile_pic_url'] = user.profile_pic.url
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                request.session['email'] = user.email
                request.session['b_date'] = str(user.b_date)
                p = str(user.phone_number)
                request.session['phone_number'] = p
                request.session['country'] = user.country
                request.session['facebook_profile'] = user.facebook_profile
                form.save()
                return render(request, 'profile_info.html')
            else:
                form = RegistrationForm(request.POST)
                for field in form:
                    print("Field Error:", field.name,  field.errors)
                return HttpResponse(form.errors)
        else:
            form = EditForm()
            return render(request, 'editprofile.html', {'form': form})
    else:
        return HttpResponseRedirect('logout')


# def update(r):
#     context = {}
#     # get courses
#     courses = Course.objects.all()
#     trainee = Trainee.objects.all()
#     context['courses'] = courses
#     context['trainees'] = trainee
#     context['id'] = 1
#     if(r.method == 'GET'):
#         return render(r, 'base.html', context)
#     else:
#         t = Trainee.objects.get(id=r.POST['tid'])
#         t.name = r.POST['name']
#         t.national = r.POST['national']
#         t.course_id_id = r.POST['course']
#         t.save()
#         return render(r, 'base.html', context)


# def CreateUserView(request):
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST, request.FILES)
#         if form.is_valid():
#             context = {}
#             context['User'] = request.session.get('username')
#             form.save()
#             return render(request, 'login.html', context)
#     else:
#         form = CreateUserForm()
#     return render(request, 'Registration.html', {'form': form})


# def list(req):
#     trainees = Trainee.objects.all()
#     for trainee in trainees:
#         print(trainee.id, trainee.name, trainee.course_id.name)
#     context = {}
#     context['title'] = 'Trainees List'
#     context['trainees'] = trainees
#     context['username'] = req.session.get('username')
#     return render(req, 'index.html', context)


# def insert(r):
#     form = RegisterTrainee(r.POST)
#     context = {}
#     # get courses
#     courses = Course.objects.all()
#     context['courses'] = courses
#     context['id'] = 1
#     print("---------------------------------"+r.method)
#     if r.method == 'GET':
#         form = RegisterTrainee()
#         return render(r, 'base.html', {'form': form})
#     else:
#         if form.is_valid():
#             nameIn = form.cleaned_data['name']
#             nationalIn = form.cleaned_data['national']
#             course_idIn = form.cleaned_data['course_id']
#             Trainee.objects.create(
#                 name=nameIn, national=nationalIn, course_id_id=course_idIn)
#             return HttpResponse('Registration Complete!')
#             # return render(r, 'base.html', {'form': form})
#         else:
#             form = RegisterTrainee()
#             return HttpResponse('Form Is Invalid!')


# def update(r):
#     context = {}
#     # get courses
#     courses = Course.objects.all()
#     trainee = Trainee.objects.all()
#     context['courses'] = courses
#     context['trainees'] = trainee
#     context['id'] = 1
#     if(r.method == 'GET'):
#         return render(r, 'base.html', context)
#     else:
#         t = Trainee.objects.get(id=r.POST['tid'])
#         t.name = r.POST['name']
#         t.national = r.POST['national']
#         t.course_id_id = r.POST['course']
#         t.save()
#         return render(r, 'base.html', context)


# class updateG(UpdateView):
#     model = Trainee
#     fields = ['name', 'national']
#     success_url = '/trainee1/list'


# def delete(r):
#     context = {}
#     # get courses
#     trainee = Trainee.objects.all()
#     context['trainees'] = trainee
#     context['id'] = 1
#     if(r.method == 'GET'):
#         return render(r, 'delete.html', context)
#     else:
#         id = r.POST['tid']
#         print(id)
#         Trainee.objects.filter(id=id).delete()
#         return render(r, 'delete.html', context)


# class deleteClass(View):

#     def get(self, r):
#         context = {}
#         # get courses
#         trainee = Trainee.objects.all()
#         context['trainees'] = trainee
#         context['id'] = 1
#         return render(r, 'base_del.html', context)

#     def post(self, r):
#         context = {}
#         # get courses
#         trainee = Trainee.objects.all()
#         context['trainees'] = trainee
#         context['id'] = 1
#         id = r.POST['tid']
#         Trainee.objects.filter(id=id).delete()
#         return render(r, 'base_del.html', context)


# def logout(r):
#     #logout(r, r.session['authUser'])
#     # print(r.session.get('authUser'))
#     auth.logout(r)
#     r.session.clear()
#     return HttpResponseRedirect('/trainee1/list')


# @api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
# def apilist(r):
#     trainees = Trainee.objects.all()
#     if (trainees is not None):
#         data = traineeSerializer(trainees, many=True)
#         print("-------------NOT NONE------------")
#         print(data)
#         s = json.dumps(data.data)
#         print(data.data)
#         print(s)
#     else:
#         print('------------ NONE------------")')
#     doc = {
#         '/': 'overview',
#         '/listapi': 'return trainees as JSON',
#         '/insertapi': 'insert trainees from JSON',
#         '/updateapi': 'updates trainees from JSON',
#         '/deleteapi': 'deletes trainees from JSON',
#     }
#     # print("------------------------------------")
#     # print(data.data)
#     # print("------------------------------------")
#     # return Response(doc)
#     return Response(data.data)


# @api_view(['POST'])
# @permission_classes((permissions.AllowAny,))
# def apiinsert(r):
#     newdata = traineeSerializer(data=r.data)
#     #result = Trainee.objects.create(newdata)
#     print(r.data)
#     if(newdata.is_valid()):
#         newdata.save()
#         return Response(newdata.data)
#     else:
#         return HttpResponse('Failed To Insert')


# @api_view(['PUT'])
# @permission_classes((permissions.AllowAny,))
# def apiupdate(request, id):
#     traineeEdit = Trainee.objects.get(pk=id)
#     edited = traineeSerializer(traineeEdit, data=request.data)
#     if(edited.is_valid()):
#         edited.save()
#         return Response(edited.data)
#     else:
#         return HttpResponse('failed')


# @api_view(['DELETE'])
# @permission_classes((permissions.AllowAny,))
# def apidelete(request, id):
#     traineeEdit = Trainee.objects.get(pk=id)
#     traineeEdit.delete()
#     return Response(status=200)


# def getcsrf():
#     pass
