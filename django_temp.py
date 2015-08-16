#!/usr/bin/env python3

import os, tempfile, json
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from django.db import connection

# Method for sending files to users
def send_file(request):
    json_file = __file__ # Select file
    wrapper = FileWrapper(file(json_file, 'rb'))
    response = HttpResponse(wrapper, content_type='application/json')
    response["Content-Length"] = os.path.getsize(json_file)
    return response


def error(msg):
    pass

# Method for populating DB from json
def import_items(region_list):
    for region in region_list:
        try:
            with open("json/item/"+region,'r') as item_file:
                item_json = json.load(item_file)
                for item_id in item_json["data"]:
                    item_id = item_id
                    
                    item = item_json["data"][item_id]
                    desc = item["sanitizedDescription"]
                    gt = item["gold"]["total"]
                    gb = item["gold"]["base"]
                    name = item["name"]
                    
                    try:
                        tags = item["tags"]
                    except KeyError:
                        tags = []
                    icon = "icons/item/"+item_id+".png"
                    try:
                        stacks = item["stacks"]
                    except KeyError:
                        stacks = 1
                    stats = item["stats"]

                    stat_list = []
                    value_list = []
                                  
                    for stat,value in stats.items():
                        stat_list.append(stat)
                        value_list.append(value)
                    
                    with connection.cursor() as cursor:
                        ex_string = "INSERT INTO ItemStat( "
                        for index, stat in enumerate(stat_list):
                            test_string = ex_string + stat + \
                                          (", " if index < len(stat_list)-1 else ") VALUES(")
                            
                        for index, value in enumerate(value_list):
                            test_string = ex_string + value + \
                                          (", " if index < len(value_list)-1 else ");")
                            
                        cursor.execute(ex_string)
                        
                    
                    item_db = Item(item_id=item_id, description=desc, gold_total=gt,
                                   gold_base=gb, name=name, tags=tags, icon=icon,
                                   stacks=stacks, stats=stats)
                    item_db.save()
                
        except FileNotFoundError:
            error("Did not find file for region "+region)        
            continue

import_items(["eune"])
