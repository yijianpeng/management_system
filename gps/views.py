from django.shortcuts import render

# Create your views here.
import requests
from django.http import JsonResponse
from .models import gps
import json

def update_location(request):
    address_point = gps.objects.all()
    address_longitude = []
    address_latitude = []
    address_data = []
    for i in range(len(address_point)):
        address_longitude.append(address_point[i].longitude)
        address_latitude.append(address_point[i].latitude)
        address_data.append(address_point[i].data)

    return render(request, 'display.html',
                  {'address_longitude': json.dumps(address_longitude),
                   'address_latitude': json.dumps(address_latitude), 'address_data': json.dumps(address_data)})


