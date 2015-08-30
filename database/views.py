import os
import tempfile
import json
from decimal import *
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
		champ_stats = "[{'MPRegen': 0, 'SpellBlock': 0, 'Crit': 0, 'AttackDamage': 0, \
						'MP': 0, 'HPRegen': 0, 'HP': 0, 'Armor': 0, 'MoveSpeed': 0, \
						'AttackSpeedOffset': 0}]"
		champion = {"Name": "None", "Icon": "icons/champion/Unknown.png"}
	else:
		champion = get_object_or_404(Champion, Name = champ_name)
		champ_stats = ChampionStat.objects.filter(ChampID = champion.ChampID).values()
	items = Item.objects.all()
	item_stats = ItemStat.objects.all().values()
	item_stats = [item for item in item_stats]
	for item in item_stats:
		for key, value in list(item.items()):
			if value == 0.00000:
				item.pop(key)

	item_list = zip(items, item_stats)
	context = {
		"champ": champion,
		"champ_stats": champ_stats,
		"item_list": item_list
	}
	return render(request, 'database/items.html', context)

def item_set(request, item_set):
	context = {"item_set" : item_set}
	return render(request, 'database/item_set.html', context)
