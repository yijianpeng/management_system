from .models import gps
import json


from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Location, Image
# Create your views here.



#在百度地图中显示
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



@api_view(['POST'])
def upload(request):
    longitude = request.data.get('longitude')
    latitude = request.data.get('latitude')
    image_file = request.FILES.get('image')

    # 保存定位信息
    location = Location.objects.create(longitude=longitude, latitude=latitude)

    # 保存图片
    image = Image.objects.create(location=location, image=image_file)

    return Response({'status': 'success'})
