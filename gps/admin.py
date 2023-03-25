from django.contrib import admin

# Register your models here.
admin.site.site_header = '车载巡检系统管理后台'  # 设置header
admin.site.site_title = '车载巡检系统管理后台'   # 设置title
admin.site.index_title = '车载巡检系统管理后台'


from .models import gps
class gps_Manager(admin.ModelAdmin):
    list_display = ['id','longitude','latitude','data']
  # 增加自定义按钮
    actions = ['custom_button']

    def custom_button(self, request, queryset):
        pass

    # 显示的文本，与django admin一致
    custom_button.short_description = '在地图中显示'
    # icon，参考element-ui icon与https://fontawesome.com
    custom_button.icon = 'fa-solid fa-map'
#<i class="fa-solid fa-map"></i>
    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    custom_button.type = 'success'

    # 给按钮追加自定义的颜色
    custom_button.style = 'color:black;'

    # 链接按钮，设置之后直接访问该链接
    # 3中打开方式
    # action_type 0=当前页内打开，1=新tab打开，2=浏览器tab打开
    # 设置了action_type，不设置url，页面内将报错
    # 设置成链接类型的按钮后，custom_button方法将不会执行。

    custom_button.action_type = 0
    custom_button.action_url = 'http://127.0.0.1:8000/location/'

admin.site.register(gps,gps_Manager)

