from django.db import models
from django.db.models import Model
# Create your models here.
class gps(models.Model):
    longitude=models.FloatField()
    latitude=models.FloatField()
    data = models.CharField(max_length=200,default='')

    class Meta:
        verbose_name = "GPS定位"
        verbose_name_plural = "GPS定位"


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')   