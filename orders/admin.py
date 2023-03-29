from django.contrib import admin
from .models import Task
# Register your models here.

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Task
from django.core.mail import send_mail


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'assigned_to','status')
    list_filter = ('assigned_to',)
    search_fields = ('name', 'description',)


    #派单任务创建页面
    actions = ['assign_task']
    def assign_task(self, request, queryset):
        for task in queryset:
            task.assigned_to = request.user.employee
            task.save()
        self.message_user(request, 'Tasks assigned successfully.')
    assign_task.short_description = 'Assign selected tasks to yourself'



    #邮件提醒功能
    def send_reminder(modeladmin, request, queryset):
        for task in queryset:
            if task.assigned_to.email:
                subject = 'Task Reminder'
                message = f'Hi {task.assigned_to.first_name},\n\nPlease remember to complete the task "{task.name}" by its due date.\n\nThanks!'
                from_email = 'noreply@example.com'
                recipient_list = [task.assigned_to.email]
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        modeladmin.message_user(request, 'Reminder email(s) sent successfully.')

    send_reminder.short_description = 'Send Reminder'
    actions = [send_reminder]




admin.site.register(Task, TaskAdmin)