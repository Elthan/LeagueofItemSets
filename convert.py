#!/usr/bin/env python3

import json
import os

def create_item_set_json(name, block_list, set_map="any", mode="any"):
    '''
Create a item set json file.

Parameters
-------------
name : str
    Name of the item set.
block_list : list[str]
    List of all the blocks in the item set.
set_map : str
    Which map should the item set be shown at.
mode : str
    Which modes should the item sets be shown in.
    '''
    item_set_string = """
{
    "title": "{name}"",
    "type": "custom",
    "map": "{set_map}",
    "mode": "{mode}",
    "priority": false,
    "sortrank": 0,
    "blocks": [
    """.format(
        name = title,
        set_map = set_map,
        mode = mode,
        blocks = block_list
    )

    # Add each block with a , inbetween unless its the last one.
    block_list_len = len(block_list)-1
    for index, block in enumerate(block_list):
        item_set_string = item_set_string + block + ("," if index < block_list_len else "")
    
    item_set_string = item_set_string + "]\n}"
    item_set_json = json.dumps(item_set_string)
    
    return item_set_json

def create_block_json(block_type, item_list, recMath="false", show_if_summoner="",
                      hide_if_summoner=""):
    '''
Create a block json.

Parameters
-------------
block_type : str
    Name of the block
item_list : list[str]
    List of all the items in the block in format {"id":"<id>","count",<count>}.
recMath : str
    If last item should have an arrow pointing towards it.
show_if_summoner : str
    If we should only show if a summoner spell is equipped.
hide_if_summoner : str
    If we should hide if a summoner spell is equipped.
    '''
    block_string = """
    {
        "type": "{block_type}",
        "recMath": {recMath},
        "minSummonerLevel": -1,
        "maxSummonerLevel": -1,
        "showIfSummonerSpell": "{show}",
        "hideIfSummonerSpell": "{hide}",
        "items": [
    """.format(
        block_type = block_type,
        recMath = recMath,
        show = show_if_summoner,
        hide = hide_if_summoner
    )

    # Add each item to the string with , inbetween unless it's the last one.
    item_list_len = len(item_list)-1
    for index, item in enumerate(item_list):
        block_string = block_string + item + ("," if index < item_list_len else "")
    block_string = block_string + "]"
        
    block_json = json.dumps(block_string)
    
    return block_json

def create_db_json_item_stats(item_json, region, log):
    '''
Create a django friendly json file for item stats.

Parameters
-------------
region : str
    Region we should convert from.
log : logging
    So we can log what is happening.
    '''
    item_id = str(item_json["id"])
    log.debug("Creating json file for item stats for item " + item_id)
    os.makedirs("json/item_stats/" + region, exist_ok=True)
    with open("json/item_stats/" + region + "/" + item_id + ".json", 'w') as item_stats_file:
        json_db_string = """[
    {
        "pk": {item_id},
        "model": "database.Item",
        "fields": {
"""
        stats_len = len(item_json["stats"])-1
        index = 0
        for key, value in item_json["stats"].items():
            json_db_string += "\t\t\"" + key + "\": " + str(value) + \
                              (",\n" if index < stats_len else "")
            index += 1
        json_db_string += """
        }
    }
]
"""
        item_stats_file.write(json_db_string)

def create_db_json_items(region, log, overwrite=False):
    '''
Create a django friendly json file for items.

Parameters
-------------
region : str
    Region we should convert from.
log : logging
    So we can log what is happening.
overwrite : bool
    If we should write over existing files.
    '''
    log.debug("Opening json/item/" + region + ".json")
    try:
        with open("json/item/"+ region + ".json", 'r') as items_file:
            items_json = json.load(items_file)

            # Check if path exists, else create it.
            os.makedirs("json/item/" + region, exist_ok=True)

            for item_id in items_json["data"]:
                item_json = items_json["data"][item_id]

                log.debug("Creating json file for item " + item_id)
                with  open("json/item/" + region + "/" + item_id + ".json", 'w') as item_json_file:
                    json_db_string = """[
    {{
        "pk" : {item_id},
        "model" : "database.Item",
        "fields" : {{
            item_id": {item_id},
            "name": "{name}",
            "description": "{description}",
            "gold_total": {gold_total},
            "gold_base": {gold_base},
            "purchable": {purchable},
            "icon": "{icon}" """.format(
                item_id = item_id,
                name = item_json["name"],
                description = item_json["sanitizedDescription"],
                gold_total = item_json["gold"]["total"],
                gold_base = item_json["gold"]["base"],
                purchable = item_json["gold"]["purchasable"],
                icon = "icons/item/" + item_id + ".png"
            )
                    try:
                        into = item_json["into"]
                        json_db_string += ",\n\t" + """ "into": {} """.format(into)
                    except KeyError:
                        pass
                    try:
                        tags = item_json["tags"]
                        json_db_string += ",\n\t" + """ "tags": {} """.format(tags)
                    except KeyError:
                        pass
                    json_db_string = json_db_string + """
        }
    }
]
"""
                    item_json_file.write(json_db_string)

                    create_db_json_item_stats(item_json, region, log)
                    
    except FileNotFoundError:
        log.error("Could not find json file for region " + region)


def create_db_json_champ():
    
    pass
