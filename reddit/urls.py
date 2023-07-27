"""django_reddit URL Configuration

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
# from django.conf.urls import url
from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.frontpage, name="frontpage"),
    re_path(r'^comments/(?P<thread_id>[0-9]+)$', views.comments, name="thread"),
    re_path(r'^submit/$', views.submit, name="submit"),
    re_path(r'^post/comment/$', views.post_comment, name="post_comment"),
    re_path(r'^vote/$', views.vote, name="vote"),
    re_path(r'^detail/(?P<submit_id>[0-9]+)$', views.detail, name="detail"),
    re_path(r'^detail/(?P<submission_id>[0-9]+)/edit/$', views.edit, name="edit"),
    re_path(r'^detail/(?P<submission_id>[0-9]+)/change/$', views.change, name="change"),

]
