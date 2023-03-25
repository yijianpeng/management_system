
from django.urls import path
from gps.views import update_location,upload
urlpatterns = [
    path('location/',update_location,name='update_location'),
    path('api/upload/',upload, name='upload'),
]
