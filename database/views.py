import os
import tempfile
import json
from decimal import *
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import *
from .scripts.convert import item_set_manager as ism, block_manager as bm, block_item_manager as bim
from .scripts.convert import create_json_from_db as json_db

def index(request):
	champ_list = Champion.objects.all()
	context = {'champ_list': champ_list}
	return render(request, 'database/index.html', context)

def item_select(request, champ_key):
	if (champ_key == "All"):
		champ_stats = "[{'MPRegen': 0, 'SpellBlock': 0, 'Crit': 0, 'AttackDamage': 0, \
						'MP': 0, 'HPRegen': 0, 'HP': 0, 'Armor': 0, 'MoveSpeed': 0, \
						'AttackSpeedOffset': 0}]"
		champion = {"Name": "All", "Icon": os.path.join(settings.BASE_DIR,settings.STATIC_URL,"Unknown.png")}
	else:
		champion = get_object_or_404(Champion, Key = champ_key)
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

@csrf_exempt
def item_set(request):
	item_set = request.POST.get("item_set", "")
	item_set_json = json.loads(item_set)
	ism_id = ism(is_title = item_set_json["name"], is_map = item_set_json["map"], new_entry = True)

	for block in item_set_json["blocks"]:
		bm_id = bm(ism_id, name = block["name"], rec_math = block["recmath"], new_entry = True)
		for item in block["items"]:
			bim(item, bm_id, count = block["items"][item],new_entry = True)
	context = {"item_set_id": ism_id}
	return render(request, 'database/item_set.html', context)

def json_string(request, ism_id):
	json_string = json_db(ism_id)
	context = {"json": json_string}
	return render(request, 'database/view_json.html', context)

# Method for sending files to users
def download(request, ism_id):
	json_string = json_db(ism_id)
	response = HttpResponse(json_string, content_type ='application/json')
	response["Content-Disposition"] = 'attachment; filename="' + ism_id + '.json"'
	return response
