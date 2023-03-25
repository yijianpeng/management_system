import pickle
from django.shortcuts import render

# Create your views here.
import requests
from django.http import JsonResponse
from .models import Image, gps
import json

import threading
import socketserver
from django.views import View
from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


def gps_data_view(request):
    if request.method == 'POST':
        gps_data = request.POST.get('gps_data')
        latitude, longitude = gps_data.split(',')
        # 在此处添加将经纬度信息存储到数据库的代码
        gpsdata = gps(latitude=latitude, longitude=longitude)
        gpsdata.save()
        return JsonResponse('GPS数据已接收')
    else:
        return JsonResponse('无效请求')

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


@csrf_exempt
def receive_image(request):
    if request.method == 'POST':
        file = request.FILES['image']
        filename = default_storage.save(file.name, ContentFile(file.read()))
        image = Image.objects.create(image=filename)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

