from django.shortcuts import render

def landing_page(request):
    return render(request,'food_app/index.html')


def login_page(request):
    return render(request,'food_app/login.html')