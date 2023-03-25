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

class Location(models.Model):
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='images')
