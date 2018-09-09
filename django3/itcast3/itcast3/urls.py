"""itcast3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import re_path
from booktest import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.index),
    re_path(r'^book/(\d+)', views.index2),
    re_path(r'^getTest1/$', views.getTest1),
    re_path(r'^getTest2/$', views.getTest2),
    re_path(r'^getTest3/$', views.getTest3),
    re_path(r'^postTest1/$', views.postTest1),
    re_path(r'^postTest2/$', views.postTest2),
    re_path(r'^cookieTest/$', views.cookieTest),
    re_path(r'^redTest1/$', views.redTest1),
    re_path(r'^redTest2/$', views.redTest2),
    re_path(r'^jsonTest1/$', views.jsonTest1),
    re_path(r'^session1/$', views.session1),
    re_path(r'^session2/$', views.session2),
    re_path(r'^session2_handle/$', views.session2_handle),
    re_path(r'^session3/$', views.session3),
]
