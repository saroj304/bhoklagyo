from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    password = models.CharField(max_length=15)
    confirm_password = models.CharField(max_length=15)
    otp = models.CharField(max_length=6)
    
