from django.db import models
from django.utils import timezone

class PlayerItemSet(models.Model):
        item_set_id = models.CharField(max_length=200, default="000") #or other field
        item_set_file = models.FileField(default="")
        item_set_date = models.DateTimeField('date created', default=timezone.now)

        #to determine returned value
        def __str__(self): 
                return self.item_set_id

        
class ItemStat(models.Model):
        item_id = models.IntegerField(default=0)
        flat_armor_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        flat_attack_speed_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        flat_block_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        flat_crit_chance_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        flat_crit_damage_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        flat_exp_bonus = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        flat_energy_pool_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        flat_energy_regen_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        flat_hp_pool_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        flat_hp_regen_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        flat_mp_pool_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        flat_mp_regen_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        flat_magic_damage_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        flat_movement_speed_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        flat_physical_damage_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        flat_spell_block_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        percent_armor_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        percent_attack_speed_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        percent_block_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        percent_crit_chance_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        percent_crit_damage_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        percent_dodge_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        percent_exp_bonus = models.DecimalField(max_digits=11, decimal_places=5, default=0)    
        percent_hp_pool_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)    
        percent_hp_regen_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        percent_life_steal_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        percent_mp_pool_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        percent_mp_regen_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        percent_magic_damage_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        percent_movement_speed_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        percent_physical_damage_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        percent_spell_block_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        percent_spell_vamp_mod = models.DecimalField(max_digits=11, decimal_places=5, default=0)

        #to determine returned value 
        def __str__(self):
                return self.item_id
        
        
class Item(models.Model):
        item_id = models.IntegerField(default=0)
        description = models.CharField(max_length=200, default="Describe me!")
        gold_total = models.SmallIntegerField(default=0)
        gold_base = models.SmallIntegerField(default=0)
        on_map = models.CharField(max_length=200, default='all')
        name = models.CharField(max_length=200, default="item_name")
        tags = models.CharField(max_length=200, default=["all", "them", "tags"])
        icon = models.CharField(max_length=200, default="icons/item/3460.png")
        stacks = models.IntegerField(default=1)
        into = models.CharField(max_length=200, default=[""])
        
        #to determine returned value 
        def __str__(self): 
                return self.item_id
        
class ChampionStat(models.Model):
        champ_id = models.IntegerField(default=0) 
        armor = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        armor_per_level = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        attack_damage = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        attack_damage_per_level = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        attack_range = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        attack_speed_offset = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        attack_speed_per_level = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        crit = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        crit_per_level = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        hp = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        hp_per_level = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        hp_regen = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        hp_regen_per_level = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        move_speed = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        mp = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        mp_per_level = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        mp_regen = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        mp_regen_per_level = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        spell_block = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        spell_block_per_level = models.DecimalField(max_digits=11, decimal_places=5, default=0)        

        #to determine returned value 
        def __str__(self):
                return self.champ_id
        
class Champion(models.Model):
        champ_id = models.IntegerField(default=0)
        name = models.CharField(max_length=200, default="Tweemo")
        icon = models.CharField(max_length=200, default="icons/champion/Unknown.png")

        #to determine returned value 
        def __str__(self):
                return self.ChampID
        
class Version(models.Model):
        region = models.CharField(max_length=200, default="eune")
        version = models.CharField(max_length=200, default="1.0.0")

        #to determine returned value 
        def __str__(self):  
                return self.Region
