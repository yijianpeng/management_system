from django.db import models
from django.db.models import Model
# Create your models here.
from django.utils import timezone

class Location(models.Model):
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    class Meta:
        verbose_name = "定位"
        verbose_name_plural = "定位"

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='images')
