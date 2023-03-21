from django.db import models
from django.db.models import Model
# Create your models here.
class gps(models.Model):
    longitude=models.FloatField()
    latitude=models.FloatField()
    data = models.CharField(max_length=200,default='')

    