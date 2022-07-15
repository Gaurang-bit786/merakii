from .models import Client
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def login_user(request):
    if not request.user.is_authenticated:
        if  request.method == 'POST':
            uname = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(username=uname,password=pwd)
            if user is not None:
                login(request,user)
                print(uname,pwd)
                return redirect('home')
        else:
            return render(request,'login.html')
    else:
        return redirect('home')

def logout_user(request):
    logout(request)
    return redirect('loginuser')


def register(request):
    if not request.user.is_authenticated:
        if  request.method == 'POST':
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 != password2:
                messages.error(request, 'Register  Again\n Repeat password  is different ')
                print(fname,lname,phone,username,email,password1,password2)
                return redirect('loginuser')
            else:
                print(fname,lname,phone,username,email,password1)
                user = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=email, password=password1)
                client = Client(user=user,first_name=fname,last_name=lname,email=email)
                user.save()
                client.save()
                return redirect('loginuser')
        else:
            return render(request,'login.html')
    else:
        return redirect('home')


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('loginuser')
    else:
        return render(request,'dashboard.html')
