from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^parkings/$', views.parking_list),
    url(r'^parkings/(?P<pk>[0-9]+)$', views.parking_detail)
]
