
from django.urls import path
from gps.views import update_location
from gps.views import receive_image
from gps.views import gps_data_view
urlpatterns = [
    path('gps-data/',gps_data_view, name='gps_data_view'),
    path('location/',update_location,name='update_location'),
    path('receive_image/', receive_image, name='receive_image'),
]
