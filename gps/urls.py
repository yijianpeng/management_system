
from django.urls import path
from gps.views import update_location

urlpatterns = [
    path('location/',update_location,name='update_location'),
]
