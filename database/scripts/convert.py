#!/usr/bin/env python3
import json
import os
import uuid
from django.utils import timezone
from database.models import PlayerItemSet, Block, BlockItem


def item_set_manager(is_title="Made by LoIS", is_map="any", is_mode="any",
                    is_sortrank=0, is_id="", new_entry=False):
    '''
Create or modify an existing item set.

Parameters
-------------
is_title : str
    Item Set title, what is displayed in-game.
is_map : str
    Which maps the item set should be displayed on.
is_sortrank : int
    Sort the item set in descending order.
is_id : str
    ID for the item set in the database, a randomly generated UUID
new_entry : bool
    If it should create a new entry in the database or update an existing one.

Returns
-------------
is_id : str
    ID of item set when it has been created or modified.
    '''
    if (new_entry):
        is_id = uuid.uuid4().hex
        is_date = timezone.now()

        # log.debug("Creating new item set with ID: " + is_id)

        pis = PlayerItemSet(
            ID = is_id,
            Title = is_title,
            Date = is_date,
            Map = is_map,
            Mode = is_mode,
            SortRank = is_sortrank
        )
    else:
        # log.debug("Modifying existing item set with ID: " + is_id)
        # Check if we can find the item set.
        try:
            pis = PlayerItemSet.objects.get(ID=is_id)
        except PlayerItemSet.DoesNotExist:
            # log.error("Could not find item set with id: " + is_id + \
                    #   " when trying to update an item set.")
            return None
        if (is_title is not pis.Title):
            pis.Title = is_title
        if (is_map is not pis.Map):
            pis.Map = is_map
        if (is_mode is not pis.Mode):
            pis.Mode = is_mode
        if (is_sortrank is not pis.SortRank):
            pis.SortRank = is_sortrank

    pis.save()
    return is_id


def block_manager(is_id = "", name = "Custom made", rec_math = "false",
                  min_sum_lvl = -1, max_sum_lvl = -1, show_sum = "", hide_sum = "",
                  block_id = -1, new_entry = False):
    '''
Create or modify an existing new block.

Parameters
-------------
is_id : str
    ID of item set the block resides in.
name : str
    Name of the block to be displayed in game.
rec_math : str
    If all the items in the block should point to the last.
min_sum_lvl : int
    Minimum level the summoner can be for this block to be viewed.
max_sum_lvl : int
    Maximum level the summoner can be for this block to be viewed.
show_sum : str
    Only show this block if a summoner spell is used.
hide_sum : str
    Hide this block if a summoner spell is used.
block_id : int
    ID of a block if we want to modify it.
new_entry : bool
    If we want to create a new block.
    '''
    if (new_entry):
        # log.debug("Creating new block for item set with ID: " + is_id)
        # Check if item set exists
        try:
            pis = PlayerItemSet.objects.get(ID=is_id)
        except PlayerItemSet.DoesNotExist:
            # log.error("Could not find item set with ID " + is_id + \
                    #   " when creating a new block.")
            return
        block = Block(
            BlockType = name,
            RecMath = rec_math,
            MinSummonerLevel = min_sum_lvl,
            MaxSummonerLevel = max_sum_lvl,
            ShowIfSummonerSpell = show_sum,
            HideIfSummonerSpell = hide_sum,
            PlayerItemSet = pis
        )
    else:
        # log.debug("Modifying block with ID " + block_id)
        # Check if block with id exists
        try:
            block = Block.objects.get(id=block_id)
        except PlayerItemSet.DoesNotExist:
            # log.error("Could not find item set when with id: " + is_id + \
                    #   " when trying to update a Block.")
            return
        if (name is not block.Type):
            block.Type = name
        if (rec_math is not block.RecMath):
            block.RecMath = rec_math
        if (min_sum_lvl is not block.MinSummonerLevel):
            block.MinSummonerLevel = min_sum_lvl
        if (max_sum_lvl is not block.MaxSummonerLevel):
            block.MaxSummonerLevel = max_sum_lvl
        if (show_sum is not block.ShowIfSummonerSpell):
            block.ShowSummonerSpell = show_sum
        if (hide_sum is not block.HideIfSummonerSpell):
            block.HideSummonerSpell = hide_sum

    block.save()
    return block.id


def block_item_manager(item_id, block_id, count = 1,
                          block_item_id = -1, new_entry = True):
    '''
Create or modify existing item inside block.

Parameters
-------------
item_id : int
    ID of item that is used
block_id : int
    ID of block the item resides in.
count : int
    Number of times the item should be bought.
block_item_id : int
    ID of an item inside a block, if we want
    to update the item.
new_entry : bool
    If we want to create a new item inside a block.
    '''
    if (new_entry):
        # log.debug("Creating new item with ID " + item_id + " for block with ID " + block_id)
        try:
            block = Block.objects.get(id = block_id)
        except Block.DoesNotExist:
            # log.error("Could not find block with id "+ block_id + " when trying to create new item.")
            return
        item = BlockItem(
            ItemID = item_id,
            Count = count,
            Block = block
        )
    else:
        # log.debug("Modifying item with ID " + item_id + " in block with ID " + block_id)
        # Check if we can find item
        try:
            item = BlockItem.objects.get(id = block_item_id)
        except BlockItem.DoesNotExist:
            # log.error("Could not find item with id " + block_item_id + " when trying to update item.")
            return
        item.count = count
    item.save()
    return item.id


def create_json_from_db(item_set_id):
    '''
Convert information from the database to a item set JSON file.

Parameters
-------------
item_set_id : int
    Item set ID that we should convert.
    '''
    from database.models import PlayerItemSet, Block, BlockItem
    import django
    django.setup()

    try:
        item_set = PlayerItemSet.objects.get(ID=item_set_id)
    except PlayerItemSet.DoesNotExist:
        log.error("Could not find the item set with given ID: " + item_set_id)
        return
    except PlayerItemSet.MultipleObjectsReturned:
        log.error("Multiple objects returned when querying for ID: " + item_set_id)

    # JSON format for item set
    item_set_string = """{{
    "title": "{name}",
    "type": "custom",
    "map": "{set_map}",
    "mode": "{mode}",
    "sortrank": {rank},
    "blocks": [
    """.format(
        name = item_set.Title,
        set_map = item_set.Map,
        mode = item_set.Mode,
        rank = item_set.SortRank
    )

    # Use a list so we can join them together at the end
    blocks_string_list = []
    blocks = item_set.block_set.all()

    # Account for index starting at 0
    blocks_len = len(blocks) - 1

    # Add all blocks
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

        # Same as with blocks, join together at the end
        items_string_list = []
        items = block.blockitem_set.all()
        items_len = len(items) - 1

        # Add all items in the block
        for index_items, item in enumerate(items):
            item_string = """{{
            "id": "{item_id}",
            "count": {count}
            """.format(
                item_id = item.ItemID,
                count = item.Count
            )

            # If it's the last item, don't add a ,
            item_string += "},\n" if index_items < items_len else "}\n"
            items_string_list.append(item_string)

        for items in items_string_list:
            block_string += items
        block_string += "\t]\n"

        # If it's the last block, don't add a ,
        block_string += "},\n" if index_blocks < blocks_len else "}"
        blocks_string_list.append(block_string)

    for block in blocks_string_list:
        item_set_string += block
    item_set_string += "\n]\n}"

    return item_set_string


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

    path = "database/static/json/item_stats/" + region + "/"

    os.makedirs(path, exist_ok=True)

    path = path + item_id + ".json"

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
    log.debug("Opening database/static/json/item/" + region + ".json")

    try:
        with open("database/static/json/item/"+ region + ".json", 'r') as items_file:
            items_json = json.load(items_file)

            # Check if path exists, else create it.
            os.makedirs("database/static/json/item/" + region + "/", exist_ok=True)

            for item_id in items_json["data"]:
                item_json = items_json["data"][item_id]

                create_db_json_item_stats(item_json, region, log)

                path =  "database/static/json/item/" + region + "/" + item_id + ".json"

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

    except OSError as err:
        log.error("Error when trying to create DB friendly JSON from items.\n" + err)
        return

    log.info("Done converting all item JSONs and item stats JSONs"+ \
             " to DB friendly JSONs for region " + region)


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

      path = "database/static/json/champ_stats/" + region + "/"

      os.makedirs(path, exist_ok=True)

      path = path + champ_name + ".json"

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
    log.debug("Opening database/static/json/champion/" + region + ".json")

    try:
        with open("database/static/json/champion/" + region + ".json", 'r') as champs_file:
            champs_json = json.load(champs_file)

            os.makedirs("database/static/json/champion/" + region + "/", exist_ok=True)

            for champ_name in champs_json["data"]:
                champ_json = champs_json["data"][champ_name]

                create_db_json_champ_stats(champ_json, region, log)

                path = "database/static/json/champion/" + region + "/" + champ_name + ".json"

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
                        icon_path = "icons/champion/" + champ_name + ".png"
                    )
                    json_db_string +=  """
                }
            }
        ]"""
                    champ_json_file.write(json_db_string)

    except OSError as err:
        log.error("Error when trying to create DB friendly JSON for champions.\n" + err)
        return

    log.info("Done converting all champion JSONs and champion stats JSONs to DB" + \
             " friendly JSONs for region " + region)
