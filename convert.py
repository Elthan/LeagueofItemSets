#!/usr/bin/env python3

import json

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
    """.format{
        name = title,
        set_map = set_map,
        mode = mode,
        blocks = block_list
    }

    # Add each block with a , inbetween unless its the last one.
    block_list_len = len(block_list)
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
    """.format{
        block_type = block_type,
        recMath = recMath,
        show = show_if_summoner,
        hide = hide_if_summoner
    }

    # Add each item to the string with , inbetween unless it's the last one.
    item_list_len = len(item_list)
    for index, item in enumerate(item_list):
        block_string = block_string + item + ("," if index < item_list_len else "")
    block_string = block_string + "]"
        
    block_json = json.dumps(block_string)
    
    return block_json
