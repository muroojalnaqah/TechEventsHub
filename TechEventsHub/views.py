from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from .models import * #import all 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import pandas as pd

global courses_data
courses_data = {}
# Create your views here.
def home(request):
    if request.user.id is not None:
        print(request.user.id)
        users = UserInfo.objects.filter(user_id=request.user.id)
        fullname = users[0].fullname
        print(users[0].fullname)
        return render(request, "home.html", {"fullname": fullname})
    else:
        return render(request, "home.html")

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
            return HttpResponseRedirect("register")
        else:
            user=User.objects.create_user(username=username, password=password)
            user.save()
            userInfo= UserInfo.objects.create(fullname=fullname, age=age, university=university, degree=degree, major=major, user_id=user.id)
            return redirect("home")
            
    

    return render(request, "register.html")

def contactus(request):
    if request.user.id is not None: 
        print(request.user.id)
        users = UserInfo.objects.filter(user_id=request.user.id)
        fullnames = users[0].fullname
        print(users[0].fullname)
        if request.method == "POST":
            fullname = request.POST['fullname']
            emailaddress = request.POST['emailaddress']
            messege = request.POST['messege']  
            contactInfo = ContactInfo.objects.create(fullname=fullname, emailaddress=emailaddress, messege=messege)
            contactInfo.save()
            return render(request, "home.html", {"fullname": fullnames})
        return render(request, "contactus.html", {"fullname": fullnames})

    elif request.method == "POST":
            fullname = request.POST['fullname']
            emailaddress = request.POST['emailaddress']
            messege = request.POST['messege']  
            contactInfo = ContactInfo.objects.create(fullname=fullname, emailaddress=emailaddress, messege=messege)
            contactInfo.save()
            #return redirect("home")
            return render(request, "home.html")

    else:
        
        return render(request,"contactus.html")
    

def user(request):
    print(request.user.id)
    users = UserInfo.objects.filter(user_id=request.user.id)
    fullname = users[0].fullname
    university = users[0].university
    major= users[0].major
    return render(request, "user.html", {"fullname": fullname,"university": university,"major": major})


def aboutus(request):
    if request.user.id is not None:
        print(request.user.id)
        users = UserInfo.objects.filter(user_id=request.user.id)
        fullname = users[0].fullname
        print(users[0].fullname)
        return render(request, "aboutus.html", {"fullname": fullname})
    else:
        return render(request, "aboutus.html")
    

@login_required(login_url="login")
def courses(request):
    excel_file='TechEventsHub\static\courses.xlsx'
    df = pd.read_excel(excel_file)
    courses_data= df.to_dict(orient='records')
    #print(f'"Courses at if statement {courses_data}"')

    #check if user exist:
    if request.user.id is not None:
        #print('inside if statement of courses')
        #print(courses_data)
        print(request.user.id)
        users = UserInfo.objects.filter(user_id=request.user.id)
        fullname = users[0].fullname
        print(users[0].fullname) 
       # print("inside courses")
        return render(request,"courses.html", {'data': courses_data, "fullname": fullname})

    return render(request,"courses.html", {'data':courses_data})



def courses_search_result(request):
    if request.method == "GET":
        query = request.GET.get('search', '')

        if query:
            excel_file='TechEventsHub\static\courses.xlsx'
            df = pd.read_excel(excel_file)
            search_results = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False, na=False).any(), axis=1)]
            results_dict = search_results.to_dict(orient='records')

            if request.user.id is not None:
                users = UserInfo.objects.filter(user_id=request.user.id)
                fullname = users[0].fullname
                context = {'data': results_dict, "fullname": fullname}
                return render(request, "courses.html", context)
            

                context = {'data': results_dict}
                return render(request, "courses.html", context)

    return render(request, "courses.html")






@login_required(login_url="login")
def events(request):
    excel_file='TechEventsHub\static\events.xlsx'
    df = pd.read_excel(excel_file)
    events_data= df.to_dict(orient='records')

    if request.user.id is not None:
        print(request.user.id)
        users = UserInfo.objects.filter(user_id=request.user.id)
        fullname = users[0].fullname
        print(users[0].fullname) 
        return render(request, "events.html", {'data':events_data, "fullname":fullname})

    

    return render(request,"events.html", {'data':events_data})


    

    

def events_search_result(request):
    print("inside events search")
    if request.method == "GET":
        query = request.GET.get('search', '')

        if query:
            excel_file='TechEventsHub\static\events.xlsx'
            df = pd.read_excel(excel_file)
            search_results = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False, na=False).any(), axis=1)]
            results_dict = search_results.to_dict(orient='records')

            if request.user.id is not None:
                users = UserInfo.objects.filter(user_id=request.user.id)
                fullname = users[0].fullname
                context = {'data': results_dict, "fullname": fullname}
                return render(request, "events.html", context)

            context = {'data': results_dict}
            return render(request, "events.html", context)

    return render(request, "events.html")

     
def useredit(request):
    print(request.user.id)
    users = UserInfo.objects.filter(user_id=request.user.id)
    fullname = users[0].fullname
    university = users[0].university
    major= users[0].major
    if request.method =="POST":
        #username= request.POST['username']
        fullname=request.POST['fullname']  
        university=request.POST['university']
        major=request.POST['major']
        print(request.user.id)
        print("inside useredit if statement")
        #users = UserInfo.objects.filter(user_id=request.user.id)
        users.update(fullname=fullname, university=university, major=major)
        return HttpResponseRedirect("user")
    return render(request, "useredit.html", {"fullname": fullname,"university": university,"major": major})

def update(request):
    if request.method =="POST":
        username= request.POST['username']
        fullname=request.POST['fullname']  
        university=request.POST['university']
        major=request.POST['major']
        print(request.user.id)

        users = UserInfo.objects.filter(user_id=request.user.id)
        users.update(username=username, fullname=fullname, university=university, major=major)
        return redirect("user")
    return render(request,"useredit.html")
    

       

def logout(request):
    auth.logout(request)
    return redirect(reverse('home'))










