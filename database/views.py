import os
import tempfile
import json
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from django.shortcuts import get_object_or_404, render
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

def test_stuff(request):
	item_list = Item.objects.all()
	context = {'item_list': item_list}
	return render(request, 'database/test_page.html', context)

def champ_select(request):
	champ_list = Champion.objects.all()
	context = {'champ_list': champ_list}
	return render(request, 'database/champion.html', context)

def item_select(request, champion_id):
	champ_stats = get_object_or_404(ChampionStat, champion_id)
	context = {"champ_stats": champ_stats}
	return render(request, 'database/items.html', context)
