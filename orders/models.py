from django.db import models
from gps.models import Location
# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=20)
    department = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = [
        ('NEW', '正在进行'),
        ('InProgress', '正在进行'),
        ('Completed', '已完成'),
    ]
    status=models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='NEW',
    )
    def __str__(self):
        return self.name
