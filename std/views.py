from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from django.contrib import messages
#from .models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login_page")
def home(request):
    std=Student.objects.all()
    return render(request,"std/home.html",{"std":std} )

@login_required(login_url="login_page")
def add_std(request):
    if request.method=="POST":
        std_roll=request.POST.get("roll")
        std_name=request.POST.get("name")
        std_email=request.POST.get("email")
        std_address=request.POST.get("address")
        std_phone=request.POST.get("phone")

        Student.objects.create(
            roll=std_roll,
            name=std_name,
            email=std_email,
            address=std_address,
            phone=std_phone
        )

        return redirect("home_page")      
    

    return render(request,'std/add_std.html')

@login_required(login_url="login_page")
def delete_std(request,roll):
    s=Student.objects.get(roll=roll)
    s.delete()
   

    return redirect("home_page")



@login_required(login_url="login_page")
def update_std(request,roll):
    s=Student.objects.get(roll=roll)
    if request.method=="POST":
        std_roll=request.POST.get("roll")
        std_name=request.POST.get("name")
        std_email=request.POST.get("email")
        std_address=request.POST.get("address")
        std_phone=request.POST.get("phone") 

        s.roll=std_roll
        s.name=std_name
        s.email=std_email
        s.address=std_address
        s.phone=std_phone

        s.save()
       
        return redirect("home_page")
    


    return render(request,'std/std_update.html',{"std":s})
   

def login_page(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=User.objects.filter(username=username)
        if  not user.exists():
            messages.info(request,"Username Invalid")
            return redirect("login_page")
        
        user=authenticate(username=username,password=password)

        if user is None:
            messages.info(request,"Invalid Password")
            return redirect("login_page")
        else:
            login(request,user)
            return redirect("home_page")

    return render(request,"std/login_page.html")


def logout_page(request):
    logout(request)
    return redirect("login_page")


def register(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=User.objects.filter(username= username)
        if user.exists():
           messages.info(request, "Username already taken")          
           return redirect("register_page")

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account created successfully.")
        return redirect("register_page")

    
    return render(request,"std/register.html")