from django.contrib import admin
from .models import Task
# Register your models here.

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'assigned_to',)
    list_filter = ('assigned_to',)
    search_fields = ('name', 'description',)

    actions = ['assign_task']

    def assign_task(self, request, queryset):
        for task in queryset:
            task.assigned_to = request.user.employee
            task.save()
        self.message_user(request, 'Tasks assigned successfully.')
    assign_task.short_description = 'Assign selected tasks to yourself'

admin.site.register(Task, TaskAdmin)