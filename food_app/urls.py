from django.contrib import admin
from django.urls import path

from . import views as food_views
urlpatterns = [
    path('', food_views.landing_page, name='landing_page'),
    
]