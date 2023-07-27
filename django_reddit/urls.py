"""repo_name URL Configuration

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
# from django.conf.urls import include, url
from django.urls import include, re_path
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    # re_path(settings.ADMIN_URL, include(admin.site.urls)),
    # re_path(settings.ADMIN_URL, include((admin.site.urls, 'admin'), namespace='admin')),
    # re_path(r'^$', TemplateView.as_view(template_name='base.html'), name="home"),
    # url(r'^users/', include('users.urls')),
    re_path(r'^', include("reddit.urls")),
    re_path(r'^', include("users.urls"))
]
