import os
import tempfile
import json
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from django.shortcuts import get_object_or_404, render
from .models import *


def index(request):
	return render(request, 'database/index.html')

# Method for sending files to users
def send_json_file(emptyarg, file_path="database", filename="test.json"):
    json_file = open('{}/{}'.format(file_path, filename), 'rb')
    response = HttpResponse(json_file, content_type ='application/json')
    response["Content-Disposition"] = 'attachment; filename="' + filename + '"'

    return response

def champ_select(request):
	champ_list = Champion.objects.all()
	context = {'champ_list': champ_list}
	return render(request, 'database/champion.html', context)

def item_select(request, champ_name):
	if (champ_name == "None"):
		champ_stats = ""
		champion = {"Name": "None", "Icon": "icons/champion/Unknown.png"}
	else:
		champion = get_object_or_404(Champion, Name=champ_name)
		champ_stats = get_object_or_404(ChampionStat, ChampID=champion.ChampID)
	items = Item.objects.all()
	item_stats = ItemStat.objects.all()
	context = {
		"champ": champion,
		"champ_stats": champ_stats,
		"items": items,
		"item_stats": item_stats
	}
	return render(request, 'database/items.html', context)

def item_set(request):
	return render(request, 'database/item_set.html')
