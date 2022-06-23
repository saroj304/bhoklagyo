from django.contrib import admin
from django.urls import path

from . import views as food_views

urlpatterns = [
   path('login/',food_views.login_page)
]