#!/usr/bin/env python3

import json
import os
from database.models import PlayerItemSet, Block, BlockItem
import django

def create_json_from_db(item_set_id):
    '''
Convert information from the database to a item set JSON file.

Parameters
-------------
item_set_id : int
    Item set ID that we should convert.
    '''
    django.setup()

    try:
        item_set = PlayerItemSet.objects.get(ItemSetID=item_set_id)
    except PlayerItemSet.DoesNotExist:
        log.error("Could not find the item set with given ID: " + item_set_id)
        return
    except PlayerItemSet.MultipleObjectsReturned:
        log.error("Multiple objects returned when querying for ID: " + item_set_id)
        
    item_set_string = """{{
    "title": "{name}"", 
    "type": "custom",
    "map": "{set_map}",
    "mode": "{mode}",
    "priority": false,
    "sortrank": 0,
    "blocks": [
    """.format(
        name = item_set.Title,
        set_map = item_set.Map,
        mode = item_set.Mode
    )
    
    blocks = item_set.block_set.all()
    blocks_len = len(blocks) - 1 
    for index_blocks, block in enumerate(blocks):
        block_string = """{{
        "type": "{block_type}",
        "minSummonerLevel": {min_sum_lvl},
        "maxSummonerLevel": {max_sum_lvl},
        "showIfSummonerSpell": "{show_sum}",
        "hideIfSummonerSpell": "{hide_sum}",
        "items": [
        """.format(
            block_type = block.BlockType,
            min_sum_lvl = block.MinSummonerLevel,
            max_sum_lvl = block.MaxSummonerLevel,
            show_sum = block.ShowIfSummonerSpell,
            hide_sum = block.HideIfSummonerSpell
        )

        items = block.blockitem_set.all()
        items_len = len(items) - 1
        for index_items, item in enumerate(items):
            item_string = """{{
            "id": "{item_id}",
            "count": {count}
            """.format(
                item_id = item.ItemID,
                count = item.Count
            )
            item_string += "},\n" if index_items < items_len else "}\n"
            block_string += item_string
        block_string += "\t]\n"
        block_string += "},\n" if index_blocks < blocks_len else "}"
        item_set_string += block_string

    item_set_string += "\n]\n}"

    # Temporary solution
    with open("database/test.json", 'w') as item_set_file:
        item_set_file.write(item_set_string)

'''
def create_item_set_json(name, block_list, set_map="any", mode="any"):
    \'''
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
    \'''
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
    \'''
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
    \'''
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
'''

def create_db_json_item_stats(item_json, region, log):
    '''
Create a django friendly json file for item stats.

Parameters
-------------
item_json : file
    JSON file of item we create stats for.
region : str
    Region we should convert from.
log : logging
    So we can log what is happening.
    '''
    item_id = str(item_json["id"])
    
    log.debug("Creating json file for item stats for item " + item_id)
    
    os.makedirs("json/item_stats/" + region, exist_ok=True)

    path = "json/item_stats/" + region + "/" + item_id + ".json"

    with open(path, 'w') as item_stats_file:
        json_db_string = """[
    {{
        "pk": {},
        "model": "database.ItemStat",
        "fields": {{
""".format(item_id)
        stats_len = len(item_json["stats"])-1
        index = 0

        # Add all the stats the item has. Don't add ,\n on last stat.
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


def create_db_json_items(region, log):
    '''
Create a django friendly json file for items.

Parameters
-------------
region : str
    Region we should convert from.
log : logging
    So we can log what is happening.
    '''
    log.debug("Opening json/item/" + region + ".json")
    
    try:
        with open("json/item/"+ region + ".json", 'r') as items_file:
            items_json = json.load(items_file)

            # Check if path exists, else create it.
            os.makedirs("json/item/" + region, exist_ok=True)

            for item_id in items_json["data"]:
                item_json = items_json["data"][item_id]

                create_db_json_item_stats(item_json, region, log)

                path = "json/item/" + region + "/" + item_id + ".json"

                log.debug("Creating json file for item " + item_id)

                with open(path, 'w') as item_json_file:
                    json_db_string = """[
    {{
        "pk" : {item_id},
        "model" : "database.Item",
        "fields" : {{
            "ItemID": {item_id},
            "Name": "{name}",
            "Description": "{description}",
            "GoldTotal": {gold_total},
            "GoldBase": {gold_base},
            "Purchasable": "{purchasable}",
            "Icon": "{icon}" """.format(
                item_id = item_id,
                name = item_json["name"],
                description = item_json["sanitizedDescription"],
                gold_total = item_json["gold"]["total"],
                gold_base = item_json["gold"]["base"],
                purchasable = item_json["gold"]["purchasable"],
                icon = "icons/item/" + item_id + ".png"
            )
                    # Not all items build into something.
                    try:
                        into = item_json["into"]
                        json_db_string += ",\n\t" + """ "Into": {} """.format(json.dumps(into))
                    except KeyError:
                        pass

                    # Not all items have a tag.
                    try:
                        tags = item_json["tags"]
                        json_db_string += ",\n\t" + """ "Tags": {} """.format(json.dumps(tags))
                    except KeyError:
                        pass
                    json_db_string += """
        }
    }
]"""
                    item_json_file.write(json_db_string)


    except OSError:
        log.error("Could not find items JSON file for region " + region)

    log.info("Done converting all item JSONs and item stat JSONs to DB friendly JSONs for region " + region)


def create_db_json_champ_stats(champ_json, region, log):
      '''
Create a django friendly json file for champion stats.

Parameters
-------------
champ_json : file
    JSON file of champ we create stats for.
region : str
    Region we should convert from.
log : logging
    So we can log what is happening.
    '''
      champ_id = champ_json["id"]
      champ_name = champ_json["name"]

      log.debug("Creating JSON file for champion stats for champion " + champ_name)

      os.makedirs("json/champ_stats/" + region, exist_ok=True)

      path = "json/champ_stats/" + region + "/" + champ_name + ".json"

      with open(path, 'w') as champ_stats_file:
          champ_stats = champ_json["stats"]
          
          # JSON that django can read
          json_db_string = """[
    {{
        "pk": "{champ_id}",
        "model": "database.ChampionStat",
        "fields": {{
            "Armor": {armor},
            "ArmorPerLevel": {armorlvl},
            "AttackDamage": {ad},
            "AttackDamagePerLevel": {adlvl},
            "AttackRange": {ar},
            "AttackSpeedOffset": {asoff},
            "AttackSpeedPerLevel": {aslvl},
            "Crit": {crit},
            "CritPerLevel": {critlvl},
            "HP": {hp},
            "HPPerLevel": {hplvl},
            "HPRegen": {hpreg},
            "HPRegenPerLevel": {hpreglvl},
            "MoveSpeed": {ms},
            "MP": {mp},
            "MPPerLevel": {mplvl},
            "MPRegen": {mpreg},
            "MPRegenPerLevel": {mpreglvl},
            "SpellBlock": {mr},
            "SpellBlockPerLevel": {mrlvl}
        }}
    }}
]
          """.format(
              champ_id = champ_id,
              armor = champ_stats["armor"],
              armorlvl = champ_stats["armorperlevel"],
              ad = champ_stats["attackdamage"],
              adlvl = champ_stats["attackdamageperlevel"],
              ar = champ_stats["attackrange"],
              asoff = champ_stats["attackspeedoffset"],
              aslvl = champ_stats["attackspeedperlevel"],
              crit = champ_stats["crit"],
              critlvl = champ_stats["critperlevel"],
              hp = champ_stats["hp"],
              hplvl = champ_stats["hpperlevel"],
              hpreg = champ_stats["hpregen"],
              hpreglvl = champ_stats["hpregenperlevel"],
              ms = champ_stats["movespeed"],
              mp = champ_stats["mp"],
              mplvl = champ_stats["mpperlevel"],
              mpreg = champ_stats["mpregen"],
              mpreglvl = champ_stats["mpregenperlevel"],
              mr = champ_stats["spellblock"],
              mrlvl = champ_stats["spellblockperlevel"]
          )

          champ_stats_file.write(json_db_string)


def create_db_json_champ(region, log):
    '''
Create a django friendly json file for champions.

Parameters
-------------
region : str
    Region we should convert from.
log : logging
    So we can log what is happening.
    '''
    log.debug("Opening json/champion/" + region + ".json")
    
    try:
        with open("json/champion/" + region + ".json", 'r') as champs_file:
            champs_json = json.load(champs_file)

            os.makedirs("json/champion/" + region, exist_ok=True)

            for champ_name in champs_json["data"]:
                champ_json = champs_json["data"][champ_name]

                create_db_json_champ_stats(champ_json, region, log)

                path = "json/champion/" + region + "/" + champ_name + ".json"

                log.debug("Creating JSON file for " + champ_name + " in region " + region)

                with open(path, 'w') as champ_json_file:
                    json_db_string = """[
    {{
        "pk" : "{champ_id}",
        "model" : "database.Champion",
        "fields" : {{
                    "ChampID": {champ_id},
                    "Name": "{champ_name}",
                    "Icon": "{icon_path}"
                    """.format(
                        champ_id = champ_json["id"],
                        champ_name = champ_name,
                        icon_path = "icons/champion/" + champ_name
                    )
                    json_db_string +=  """
        }
    }
]"""
                    champ_json_file.write(json_db_string)
                    
    except OSError:
        log.error("Could not find champion JSON file for region " + region)

    log.info("Done converting all champion JSONs and champion stats JSONs to DB friendly JSONs for region " + region)
