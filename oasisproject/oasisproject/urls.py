"""oasisproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from myapp import views as myapp_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp_views.home, name='home'),
    path('tempindex/', myapp_views.tempindex, name='tempindex'),
    path('map/', myapp_views.map, name='map'),
    path('map1/', myapp_views.searchshow, name='searchshow'),
    path('yeosu/', myapp_views.yeosu, name='yeosu'),
    path('jeonju/', myapp_views.jeonju, name='jeonju'),
    path('wando/', myapp_views.wando, name='wando'),
    path('product/', myapp_views.productshow, name='product'),
    path('detail/<int:product_id>', myapp_views.detail, name='detail'),
    path('mypage/', myapp_views.mypage, name='mypage'),
    path('mypage2/', myapp_views.mypage2, name='mypage2'),
    path('gwangyang/', myapp_views.gwangyang, name='gwangyang'),
    path('goheung/', myapp_views.goheung, name='goheung'),
]
