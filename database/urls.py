from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^sendJSON$', views.send_json_file, name='Send JSON'),
]