from django.contrib import admin
from django.urls import path
from . import views as user_views

urlpatterns = [
    path('signup/',user_views.signup_page),
   path('login/',user_views.login_page)
]