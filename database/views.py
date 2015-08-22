import os
import tempfile
import json
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
	return render(request, 'database/index.html')

# Method for sending files to users
def send_json_file(emptyarg, file_path="database", filename="test.json"):
    json_file = open('{}/{}'.format(file_path, filename), 'rb')
    response = HttpResponse(json_file, content_type ='application/json')
    response["Content-Disposition"] = 'attachment; filename="' + filename + '"'

    return response

def rend(request):
	dicti = Version.objects.all()
	context = {'dicti': dicti}
	return render(request, 'database/index2.html', context)

def test_stuff(request):
	item_list = Item.objects.all()
	template = loader.get_template('database/test_page.html')
	context = RequestContext(request, {'item_list': item_list})
	return HttpResponse()
