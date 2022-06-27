from django.contrib import admin
from django.urls import path
from . import views as restaurant_views

urlpatterns = [
    path('register/',restaurant_views.signup_page, name='signup'),
]