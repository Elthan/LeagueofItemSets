from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^champion', views.champ_select, name='champion'),
    url(r'^items/([A-Za-z\']+)/*', views.item_select, name='items'),
    url(r'^$', views.index, name='index'),
    url(r'^sendJSON$', views.send_json_file, name='Send JSON')
]
