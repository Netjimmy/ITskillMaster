"""mywork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
from views import welcome, index, login, register
from django.contrib.auth.views import  logout
from restaurants.views import menu, meta, list_restaurants, comment
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^menu/(\d{1,5})/$', menu),
    url(r'^meta/$', meta),
    url(r'^welcome/$',welcome),
    url(r'^restaurants_list/$',login_required(list_restaurants)),
    url(r'^comment/(\d{1,5})/$',comment),
    url(r'^accounts/login/$',login),
    url(r'^accounts/logout/$',logout),
    url(r'^index/$',index),
	url(r'^accounts/register/$',register),
]
