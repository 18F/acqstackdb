"""acqstackdb URL Configuration

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

from acquisitions import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^acquisition/(?P<id>\d*)$', views.acquisition, name='acquisition'),
    url(r'^acquisition/(?P<id>\d*)/edit$',
        views.edit_acquisition,
        name='edit acquisition'
        ),
    url(r'^stages$', views.stages, name='stages'),
    url(r'^new/$', views.new_index, name='new_index'),
    url(r'^new/(?P<item>\w*)$', views.new, name="new"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^chaining/', include('smart_selects.urls')),
]
