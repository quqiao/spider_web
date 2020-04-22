"""spider_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from spider_page import views
from . import longyi_tjzq_db

urlpatterns = [
    url('^$', views.index),
    url('^page$', views.page),
    # url(r'^longyi_tjzq$', longyi_tjzq_db.slec_all),
    url(r'^rjyiyao_xpsj/', views.rjyiyao_xpsj),
    url(r'^longyi_tjzq/', views.longyi_tjzq),
    url(r'^scjrm_zszq/', views.scjrm_zszq),
    url(r"rjyiyao", views.start_rjyiyao_xpsj, name="reg1"),
    url(r"longyi", views.start_longyi_tjzq, name="reg2"),
    url(r"scjrm", views.start_scjrm_zszq, name="reg3"),
    # url('^', views.start_rjyiyao_xpsj),
    # url('^', views.start_longyi_tjzq),
]
