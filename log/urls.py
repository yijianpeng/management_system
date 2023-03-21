from log.views import login,logon,logout,index
from django.urls import path

urlpatterns = [
    path('',index,name='login'),
    path('index/',index,name='index'),
    path("logon/",logon,name='logon'),
    path("logout/",logout,name='logout'),
]