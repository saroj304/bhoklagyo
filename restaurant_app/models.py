from django.db import models


# Create your models here.clear

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    pan_no = models.CharField(max_length=10)
    long = models.FloatField()
    lat = models.FloatField()
