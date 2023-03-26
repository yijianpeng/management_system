# urls.py
from django.urls import path

from .views import assign_task_view

app_name = 'tasks'

urlpatterns = [
    path('assign_task/', assign_task_view, name='assign_task'),
]
