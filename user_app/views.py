from django.shortcuts import render
from .models import User
# Create your views here.

def signup_page(request):
    return render(request,'user_app/signup.html')

def login_page(request):
    return render(request,'user_app/login.html')