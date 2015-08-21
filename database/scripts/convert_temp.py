import django
django.setup()
from database.models import PlayerItemSet, Block, BlockItem
import uuid
import datetime


def modify_item_set(is_title="Made by LoIS", is_map="any", is_mode="any", is_sortrank=0, is_id="", new_entry=False):
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
    '''
    if (new_entry):
        is_id = uuid.uuid4().hex
        is_date = datetime.datetime.today()
        
        log.debug("Creating new item set with ID: " + is_id)
        
        pis = PlayerItemSet(
            ID = is_id, 
            Title = is_title,
            Date = is_date,
            Map = is_map,
            Mode = is_mode,
            SortRank = is_sortrank
        )
    else:
        log.debug("Modifying existing item set with ID: " + is_id)
        # Check if we can find the item set.
        try:
            pis = PlayerItemSet.objects.get(ID=is_id)
        except PlayerItemSet.DoesNotExist:
            log.error("Could not find item set with id: " + is_id + " when trying to update an item set.")
            return
        if (is_title is not pis.Title):
            pis.Title = is_title
        if (is_map is not pis.Map):
            pis.map = is_map
        if (is_mode is not pis.Mode):
            pis.mode = is_mode
        if (is_sortrank is not pis.SortRank):
            pis.SortRank = is_sortrank
    pis.save()
    

def modify_new_block(is_id = "", name="Custom made", rec_math="false", min_sum_lvl=-1, max_sum_lvl=-1,
                        show_sum="", hide_sum="", block_id=-1, new_entry=False):
    '''
Create or modify an existing new block.

Parameters
-------------
is_id : str
    
    '''
    if (new_entry):
        # Check if item set exists
        try:
            PlayerItemSet.objects.get(ID=is_id)
        except PlayerItemSet.DoesNotExist:
            log.error("Could not find item set with ID " + is_id + " when creating a new block.")
            return
        block = Block(
            BlockType = name,
            RecMath = rec_math,
            MinSummonerLevel = min_sum_lvl,
            MaxSummonerLevel = max_sum_lvl,
            ShowSummonerSpell = show_sum,
            HideSummonerSpell = hide_sum,
            PlayerItemSet = is_id
        )
    else:
        # Check if block with id exists
        try:
            block = Block.objects.get(id=block_id)
        except PlayerItemSet.DoesNotExist:
            log.error("Could not find item set when with id: " + is_id + " when trying to update a Block.")
            return
        if (name is not block.Type):
            block.Type = name
        if (rec_math is not block.RecMath):
            block.RecMath = rec_math
        if (min_sum_lvl is not block.MinSummonerLevel):
            block.MinSummonerLevel = min_sum_lvl
        if (max_sum_lvl is not block.MaxSummonerLevel):
            block.MaxSummonerLevel = max_sum_lvl
        if (show_sum is not block.ShowSummonerSpell):
            block.ShowSummonerSpell = show_sum
        if (hide_sum is not block.HideSummonerSpell):
            block.HideSummonerSpell = hide_sum
    block.save()
  
  
def modify_new_block_item(item_id, block_id=-1, count=1, block_item_id = -1, new_entry=True):
    if (not new_entry):
        # Check if we can find item
        try:
            item = BlockItem.objects.get(id = block_item_id)
        except BlockItem.DoesNotExist:
            log.error("Could not find item with id " + block_item_id + " when trying to update item.")
            return
        item.count = count
    else:
        try:
            Block.objects.get(id = block_id)
        except Block.DoesNotExist:
            log.error("Could not find block with id "+ block_id + " when trying to create new item.")
        item = BlockItem(
            ItemID = item_id,
            Count = count,
            Block = block_id
        )
    item.save()
