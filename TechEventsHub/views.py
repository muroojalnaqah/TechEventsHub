from django.shortcuts import render, redirect, HttpResponseRedirect 
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from .models import * #import all 
from django.contrib import messages


# Create your views here.
def home(request):
    #user=auth.authenticate(username=username, password=password)
    print(request.user.id)
    users = UserInfo.objects.filter(user_id=request.user.id)
    fullname = users[0].fullname
    #print(users[0].fullname)
    return render(request, "home.html", {"fullname": fullname})

def login(request):
    if request.method =="POST":
        username= request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("home")
        else:
            messages.info(request, "Invalid Username or Password")
            return HttpResponseRedirect("login")


    return render(request, "login.html")

def register(request):
    if request.method =="POST":
        username= request.POST['username']
        fullname=request.POST['fullname']
        password=request.POST['password']
        age=request.POST['age']
        university=request.POST['university']
        degree=request.POST['degree']
        major=request.POST['major']

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username is already taken")
            return HttpResponseRedirect("contactus")
        else:
            user=User.objects.create_user(username=username, password=password)
            user.save()
            userInfo= UserInfo.objects.create(fullname=fullname, age=age, university=university, degree=degree, major=major, user_id=user.id)
            return redirect("home")
            
    

    return render(request, "register.html")

def contactus(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        emailaddress = request.POST['emailaddress']
        messege = request.POST['messege']

        
        
            
        contactInfo = ContactInfo.objects.create(fullname=fullname, emailaddress=emailaddress, messege=messege)
        contactInfo.save()
        return redirect("home")
    return render(request,"contactus.html")
    

def user(request):
    print(request.user.id)
    users = UserInfo.objects.filter(user_id=request.user.id)
    fullname = users[0].fullname
    university = users[0].university
    major= users[0].major
    return render(request, "user.html", {"fullname": fullname,"university": university,"major": major})


def aboutus(request):
    return render(request, "aboutus.html")









