from django.conf.urls import include, url

from locations import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'districts/$', views.geo_districts_index),
    url(r'districts/1/$', views.geodistrict_detail),
]