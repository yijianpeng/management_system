from django.contrib import admin
from .models import Location
# Register your models here.
admin.site.site_header = '车载巡检系统管理后台'  # 设置header
admin.site.site_title = '车载巡检系统管理后台'   # 设置title
admin.site.index_title = '车载巡检系统管理后台'



class Location_Admin(admin.ModelAdmin):
    list_display = ('id','longitude', 'latitude')
   
    # 增加自定义按钮
    actions = ['make_copy', 'custom_button']

    def custom_button(self, request, queryset):
        pass

    # 显示的文本，与django admin一致
    custom_button.short_description = '测试按钮'
    # icon，参考element-ui icon与https://fontawesome.com
    custom_button.icon = 'fas fa-audio-description'

    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    custom_button.type = 'danger'

    # 给按钮追加自定义的颜色
    custom_button.style = 'color:black;'

    def make_copy(self, request, queryset):
        pass
    make_copy.short_description = '复制员工'


admin.site.register(Location, Location_Admin)