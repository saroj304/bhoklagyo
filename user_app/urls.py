from django.contrib import admin
from django.urls import path
from . import views as user_views

urlpatterns = [
    path('signup/',user_views.signup_page, name='signup'),
    path('login/',user_views.login_page, name='login'),
    path('register/',user_views.register, name='register'),
    path('authenticate/',user_views.login_user, name='authenticate'),
]
