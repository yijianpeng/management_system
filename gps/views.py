import json
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Location, Image

from django.views.decorators.csrf import csrf_exempt


# Create your views here.



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



#在百度地图中显示
def update_location(request):
    if request.method == 'POST':
        address_point = Location.objects.all()
        address_longitude = []
        address_latitude = []
        address_data = []
        for i in range(len(address_point)):
            address_longitude.append(address_point[i].longitude)
            address_latitude.append(address_point[i].latitude)
            address_data.append('施工地点')
    return render(request, 'display.html',
                  {'address_longitude': json.dumps(address_longitude),
                   'address_latitude': json.dumps(address_latitude), 'address_data': json.dumps(address_data)})

@csrf_exempt
def map_view(request):
    locations = Location.objects.all()
    data = []
    for loc in locations:
        images = Image.objects.filter(location_id=loc.id)
        img_urls = [img.image.url for img in images]
        data.append({
            'lng': loc.longitude,
            'lat': loc.latitude,
            'images': img_urls
        })
    return JsonResponse({'data': data})

#页面显示
def map_page(request):
    return render(request, 'map.html')