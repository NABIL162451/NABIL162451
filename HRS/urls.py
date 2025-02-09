"""
URL configuration for HRS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from HRSApp import views 
from HRSApp.models import *
from HRS import views
app_name = 'HRSApp'
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.sign_up,name='signup'),
    path('login/', views.login_page, name='login'),   
    path('login/home/', views.home_page, name='home'), 
    path('login/logout/', views.LogoutPage, name='logout'), 
    path('login/profile/', views.profile, name='profile'),
    path('login/RentPost/', views.RentPost, name='RentPost'),
    path('login/search_results/', views.search_results, name='search_results'),
    # path('login/api/get_house/' ,views.get_house, name = 'getHouse'),
    path('login/index/', views.index, name='index'),
    path('', include('HRSApp.urls')),


] 

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)