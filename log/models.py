from django.db import models
from django.db.models import Model
# Create your models here.
class Account(models.Model):
    password=models.CharField(max_length=200)
    name=models.CharField(max_length=20)