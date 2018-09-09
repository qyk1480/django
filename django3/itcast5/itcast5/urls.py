"""itcast5 URL Configuration

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
    re_path('^index/$', views.index),
    re_path('^myexp/$', views.myexp),
    re_path('^uploadPic/$', views.uploadPic),
    re_path('^uploadHandle/$', views.uploadHandle),
    re_path('^herolist/(\d*)/*$', views.herolist),
    re_path('^area/$', views.area),
    re_path('^area/(\d+)/$', views.area2),
]
