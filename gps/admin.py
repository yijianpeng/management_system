from django.contrib import admin
from .models import Location
# Register your models here.
admin.site.site_header = '车载巡检系统管理后台'  # 设置header
admin.site.site_title = '车载巡检系统管理后台'   # 设置title
admin.site.index_title = '车载巡检系统管理后台'



class Location_Admin(admin.ModelAdmin):
    list_display = ('id','longitude', 'latitude')
   
admin.site.register(Location, Location_Admin)