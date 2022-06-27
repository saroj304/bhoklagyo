from django.shortcuts import render

from django.http import HttpResponse
from restaurant_app.models import Restaurant


# Create your views here.
def signup_page(request):
    if request.method == 'POST':

        return render(request, '/')
    else:
        return render(request, 'restaurant_app/signup.html')
