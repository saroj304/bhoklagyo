from django.shortcuts import render


def landing_page(request):
    return render(request, 'food_app/index.html')


