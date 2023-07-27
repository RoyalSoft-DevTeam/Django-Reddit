# from django.conf.urls import url
from django.urls import re_path, path

from . import views

urlpatterns = [
    re_path(r'^register/$', views.register, name="register"),
    re_path(r'^login/$', views.user_login, name="login"),
    re_path(r'^logout/$', views.user_logout, name="logout"),
    re_path(r'^user/(?P<username>[0-9a-zA-Z_]*)$', views.user_profile, name="user_profile"),
    re_path(r'^profile/edit/$', views.edit_profile, name="edit_profile"),
]
