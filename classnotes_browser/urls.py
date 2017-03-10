# -*- coding: utf-8 -*-
"""Dynamically generate url for markdown files"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^cours/(\w+)/$', views.cours_dir, name="subject"),
    url(r'^cours/(\w+)/(.+)/$', views.render_md, name="cours-file")
]
