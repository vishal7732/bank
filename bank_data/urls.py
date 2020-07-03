
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    #path('bankdetail', views.bankdetail, name="bankdetail"),
    path('get_info', views.get_info, name="get_info"),
    path('name', views.name, name="name"),
    path('get_info_city', views.get_info_city, name="get_info_city"),
]
    
