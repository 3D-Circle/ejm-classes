# -*- coding: utf-8 -*-
"""Dynamically generate url for markdown files"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^cours/(\w+)/$', views.cours_dir, name="subject"),
    url(r'^cours/(\w+)/(\w+)/$', views.render_md, name="cours-file"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
