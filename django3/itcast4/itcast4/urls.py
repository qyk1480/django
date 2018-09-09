"""itcast4 URL Configuration

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
    re_path('^$', views.index, name = 'index'),
    re_path('^(\d+)/(\d+)/$', views.show, name = 'show'),
    re_path('^index2/$', views.index2, name = 'index2'),
    re_path('^htmlTest/$', views.htmlTest, name = 'htmlTest'),
    re_path('^csrf1/$', views.csrf1, name = 'csrf1'),
    re_path('^csrf2/$', views.csrf2, name = 'csrf2'),
    re_path('^verifycode/$', views.verifycode)
]
