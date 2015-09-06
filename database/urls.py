from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^itemset$', views.item_set, name='itemset'),
    url(r'^json&id=([\w\d]+)$', views.json_string, name='json'),
    url(r'^download&id=([\w\d]+)$', views.download, name='download'),
    url(r'^([\w]+)/*$', views.item_select, name='items'),
    url(r'^$', views.index, name='index'),
]
