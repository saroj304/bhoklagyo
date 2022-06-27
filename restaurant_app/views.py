from django.shortcuts import render

from django.http import HttpResponse
from restaurant_app.models import Restaurant


# Create your views here.
def signup_page(request):
    if request.method == 'POST':
        name = request.POST['rest_name']
        city = request.POST['city']
        province = request.POST['province']
        postalcode = int(request.POST['postalcode'])
        if(name==''||city==''||):
        restaurant = Restaurant(rest_name=name, city=city, province=province, postalcode=postalcode)
        restaurant.save()
        return render(request, '/')
    else:
        return render(request, 'restaurant_app/signup.html')
