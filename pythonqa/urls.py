"""pythonqa URL Configuration

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
from django.conf.urls import url, include

import debug_toolbar

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


admin.sites.AdminSite.site_header = 'QA管理系统'
admin.sites.AdminSite.site_title = '标题党'
admin.sites.AdminSite.index_title = '你想干嘛就干嘛'

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    url(r'^', include('qa.urls')),
    url(r'^', include('core.urls')),
]
