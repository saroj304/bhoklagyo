from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=14)
    password = models.CharField(max_length=200)
    #confirm_password = models.CharField(max_length=15)
    #otp = models.CharField(max_length=6)
    
