from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.

def signup_page(request):
    return render(request,'user_app/signup.html')

def login_page(request):
    return render(request,'user_app/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = make_password(request.POST['password'])
        #password =request.POST['password']
        check_password=User.objects.filter(phone=phone).exists()
        if check_password:
            return redirect('signup')
        else:
            user = User.objects.create(first_name=first_name,last_name=last_name,email=email,phone=phone,password=password)
            return redirect("landing_page")
            
    else:
        return HttpResponse('signup')    
        
def getPassword(request):
    if request.method == 'POST':
        userpassword = User.objects.filter(username='s')
        for userdata in userpassword:
            password = userdata.password
            print(password)
            if check_password(7,password):
                return HttpResponse(password)
            else:
                return HttpResponse("suck")
    