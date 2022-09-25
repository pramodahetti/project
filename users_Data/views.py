from mimetypes import init
from urllib import request
from users_Data.models import users
from django.contrib.auth import authenticate
from django.shortcuts import render,HttpResponse
user=None
def home(requests):
           return render(requests,'mywebsite.html',{'message':'#login'})
def logged(requests):
           name=requests.POST['username']
           passw=requests.POST['password']
           check=authenticate(username=name,password=passw)
           if check!=None:
               global user
               user=name
               return render(requests,'mywebsite.html',{'message':name})
           else:
               return render(requests,'mywebsite.html',{'message':'login'})
def register(requests):
    return render(requests,'register.html')
def login(requests):
    return render(requests,'login.html')
def about(requests):
    return render(requests,'login.html')
