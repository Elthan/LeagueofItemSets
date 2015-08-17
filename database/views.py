import os
import tempfile
import json
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from django.shortcuts import render
# Create your views here.


# Method for sending files to users
def send_json_file (emptyarg, file_path="database", filename="test.json"):
    json_file = open('{}/{}'.format(file_path, filename), 'rb')
    response = HttpResponse(json_file, content_type ='application/json')
    response["Content-Disposition"] = 'attachment; filename="' + filename + '"'

    '''
    json_file = open(file_path, 'rb')# Select file
    wrapper = FileWrapper(file(json_file, 'rb'))
    response = HttpResponse(wrapper, content_type='application/json')
    response["Content-Length"] = os.path.getsize(json_file)
    '''
    return response
