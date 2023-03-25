
from django.urls import path
from gps.views import update_location,upload,map_view,map_page
urlpatterns = [
    path('location/',update_location,name='update_location'),
    path('api/upload/',upload, name='upload'),
    path('map-data/', map_view, name='map_data'),
    path('map/',map_page, name='map_page'),
]
