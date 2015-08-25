from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^championselect', views.champ_select, name='champion'),
    url(r'^([\w]+)/*$', views.item_select, name='items'),
    url(r'^$', views.index, name='index'),
    url(r'^sendJSON$', views.send_json_file, name='Send JSON')
]
