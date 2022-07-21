"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.template.defaulttags import url
from django.urls import path, re_path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',welcome),    #获取菜单
    path('home/',home),    #进入首页
    path('login/',login),   #进入登录页面
    re_path('child/(?P<eid>.+)/(?P<oid>.*)/',child),    #进入子页面
    path('login_action/',login_action),   #登录
    path('register_action/',register_action), #注册
    path('accounts/login/',login), #没有登录的时候，自动重定向到登录页
    path('logout/',logout),  #退出登录
    path('pei/',pei)  #吐槽文本框
]
