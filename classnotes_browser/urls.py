from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^cours/(.+)/(.+)/$', views.render_md, name="cours")
]
