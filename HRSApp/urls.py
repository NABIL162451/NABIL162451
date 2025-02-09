
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from HRSApp import views
from HRSApp.models import *
from HRS import views
from django.urls import path
from . import views


urlpatterns = [
    
    
    # path('HouseDetails/', views.HouseDetails,name='HouseDetails'),
    path('create_profile/', views.create_profile, name='create_profile'),
    
]
