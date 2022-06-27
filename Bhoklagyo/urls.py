"""Bhoklagyo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from food_app import views as food_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food_app/',include('food_app.urls')),
    path('', food_views.landing_page, name ='landing_page'),
    path('user_app/',include('user_app.urls')),
<<<<<<< HEAD

=======
    path('authentication_app/', include('authentication_app.urls'))
>>>>>>> b42c6c1b83bbf0618fac4a49821434f018f8bfc3
]
git