from django.db import models


# Create your models here.
class Restaurant(models.Model):
    pan_no = models.CharField(max_length=10)
    lon = models.FloatField()
    lat = models.FloatField()
