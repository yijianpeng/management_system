from django.contrib import admin
from .models import Task
# Register your models here.

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Task
from django.core.mail import send_mail


class TaskAdmin(admin.ModelAdmin):
    
    empty_value_display = "default" #列数据为空时默认显示
    list_display = ('name', 'location','description', 'assigned_to','created_at','status','updated_at')
    ordering = ('-id',) #按照ID进行排序
    list_editable = ['status']
    list_display_links = ('name',)
    list_filter = ('assigned_to','status') #过滤器
    search_fields = ('name', 'description',) #搜索

    #邮件提醒功能
    def send_reminder(modeladmin, request, queryset):
        for task in queryset:
            if task.assigned_to.email:
                subject = 'Task Reminder'
                message = f'Hi {task.assigned_to.name},\n\nPlease remember to complete the task "{task.name}" by its due date.\n\nThanks!'
                from_email = '2531942094@qq.com'
                recipient_list = [task.assigned_to.email]
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        modeladmin.message_user(request, 'Reminder email(s) sent successfully.')

    send_reminder.short_description = ' 邮件通知'
    # icon，参考element-ui icon与https://fontawesome.com
    send_reminder.icon = 'fa-sharp fa-solid fa-envelope '
    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    send_reminder.type = 'primary'
    # 给按钮追加自定义的颜色
    send_reminder.style = 'color:black;'
    send_reminder.confirm='是否要向所选运维组员工发送邮件提醒？'



    #按钮注册功能
    actions = [send_reminder,]


admin.site.register(Task, TaskAdmin)