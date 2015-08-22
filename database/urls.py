from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sendJSON$', views.send_json_file, name='Send JSON'),
    url(r'^index', views.index, name='index'),
    url(r'^test', views.test_stuff, name='test'),
    url(r'^itemset', views.item_set, name='itemset'),
    url(r'^$', views.rend, name='render')
]
