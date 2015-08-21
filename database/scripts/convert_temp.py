import django
django.setup()
from database.models import PlayerItemSet, Block, BlockItem
import uuid
import datetime


def create_new_item_set(is_title="Made by LoIS", is_map="any", is_mode="any", is_sortrank=0):
    is_id = uuid.uuid4().hex
    is_date = datetime.datetime.today()
    
    pis = PlayerItemSet(
      ID = is_id, 
      Title = is_title,
      Date = is_date,
      Map = is_map,
      Mode = is_mode,
      SortRank = is_sortrank
    )
    pis.save() 
    
    
  def create_new_block(is_id, name="Custom made", rec_math="false", min_sum_lvl=-1, max_sum_lvl=-1, show_sum="", hide_sum=""):
    block = Block(
      BlockType = name,
      RecMath = rec_math,
      MinSummonerLevel = min_sum_lvl,
      MaxSummonerLevel = max_sum_lvl,
      ShowSummonerSpell = show_sum,
      HideSummonerSpell = hide_sum,
      PlayerItemSet = is_id
    )
    block.save()
  
  
def create_new_block_item(block_id, item_id, count=1):
  item = Item(
    ItemID = item_id,
    Count = count,
    Block = block_id
  )
  item.save()
