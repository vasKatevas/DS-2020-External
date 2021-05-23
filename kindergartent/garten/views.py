from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
import garten.models
from garten.models import *
import requests
from requests import session
import uuid
from django.conf import settings as garten_settings

def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def application(request):
    if request.user.is_authenticated:
        return render(request,'application.html')
    else:
        return render(request,'login.html')


def registerform(request):

    if(request.method=='POST'):
       username=request.POST['username']
       email=request.POST['email']
       password=request.POST['password']
       password1=request.POST['password1']
       if(password1==password):
        if(User.objects.filter(username=username).exists()==False):
         if(User.objects.filter(email=email).exists()==False):   
          user=User.objects.create_user(username=username,password=password1,email=email)
          user.save()
          print("user added")
          return redirect('/')
         else:
             return render(request,'register.html',{'lol':'email is taken'})
        else:
            return render(request,'register.html',{'lol':'username does exist'})
       else:
           return render(request,'register.html',{'lol':'Passwords are not the same'})
    else:
        return render(request,'index.html')

def loginform(request):
    if(request.method=='POST'):
       username=request.POST['username']
       password=request.POST['password']
       user=auth.authenticate(username=username,password=password)
       if(user is not None):
           auth.login(request,user)
           return redirect('/')
       else:
            return render(request,'login.html',{'lol':"wrong password or username!"})

def logout(request):
    auth.logout(request)
    return redirect('/')

def applyform(request):


    api_url= garten_settings.GARTEN_POST_API


    if request.user.is_authenticated:

        if(request.method=='POST'):
            principal=request.user.username
            parent_first_name=request.POST['parent_first_name']
            parent_last_name=request.POST['parent_last_name']
            income=int(request.POST['income'])
            child_first_name=request.POST['child_first_name']
            child_last_name=request.POST['child_last_name']
            age=int(request.POST['age'])

            url= api_url+"/applications"
            data={
                "username":principal,
                "parentFirstName":parent_first_name,
                "parentLastName":parent_last_name,
                "income":int(income),
                "childFirstName":child_first_name,
                "childLastName":child_last_name,
                "age":int(age)
            }

            cookie=str(uuid.uuid4())
            loginData='username=external&password=pass123'
            headers = {
                'Authorization': 'Basic YWRtaW46MjU0MjAwMA==',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'JSESSIONID='+cookie
            }

            with session() as c:
                c.post(api_url+"/authUser", headers=headers, data=loginData)
                response = c.post(url, data=data)
                print(response)
                return redirect('/')
        else:
                return redirect('/')
    else:
        return redirect('login.html')
