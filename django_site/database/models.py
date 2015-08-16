from django.db import models
from django.utils import timezone

class PlayerItemSet(models.Model):
	ItemSetID= models.CharField(max_length=200, default="000") #or other field
	ItemSetFile = models.FileField(default="")
	ItemSetDate = models.DateTimeField('date created', default=timezone.now)
	def __str__(self):              #to determine returned value 
       	 		return self.item_set_id
       	 		
class ItemStat(models.Model):
	ItemID = models.CharField(max_length=200, default="000")
	FlatArmorMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	FlatAttackSpeedMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	FlatBlockMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	FlatCritChanceMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	FlatCritDamageMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	FlatExpBonus = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	FlatEnergyPoolMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	FlatEnergyRegenMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	FlatHPPoolMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	FlatHPRegenMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	FlatMPPoolMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	FlatMPRegenMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	FlatMagicDamageMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	FlatMovementSpeedMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	FlatPhysicalDamageMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	FlatSpellBlockMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	PercentArmorMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	PercentAttackSpeedMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	PercentBlockMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	PercentCritChanceMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	PercentCritDamageMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	PercentDodgeMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	PercentExpBonus = models.DecimalField(max_digits=11, decimal_places=5, default=0)	
	PercentHPPoolMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)	
	PercentHPRegenMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	PercentLifeStealMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	PercentMPPoolMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	PercentMPRegenMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	PercentMagicDamageMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	PercentMovementSpeedMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	PercentPhysicalDamageMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	PercentSpellBlockMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	PercentSpellVampMod = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	def __str__(self):              #to determine returned value 
       	 		return self.item_id
       	 		
class Item(models.Model):
	ItemID = models.CharField(max_length=200, default="000")
	Description = models.CharField(max_length=200, default="Describe me!")
	GoldTotal= models.SmallIntegerField(default=0)
	GoldBase = models.SmallIntegerField(default=0)
	Name = models.CharField(max_length=200, default="itemname")
	Tags = models.CharField(max_length=200, default=["all", "them", "tags"])
	Icon = models.CharField(max_length=200, default="../icons/item/3460.png")
	Stacks = models.BooleanField(default=1)
	def __str__(self):              #to determine returned value 
       	 		return self.item_id
        	 		
class ChampionStat(models.Model):
	ChampID = models.CharField(max_length=200, default="000") 
	Armor = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	ArmorPerLevel = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	AttackDamage = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	AttackDamagePerLeve = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	AttackRange = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	AttackSpeedOffset = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	AttackSpeedPerLevel = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	Crit = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	CritPerLevel = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	HP = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	HPPerLevel = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	HPRegen = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	HPRegenPerLevelhp_regen_per_level = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	move_speed = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	mp = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	mp_per_level = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	mp_regen = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	mp_regen_per_level = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	spell_block = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	spell_block_per_level = models.DecimalField(max_digits=11, decimal_places=5, default=0)
	def __str__(self):              #to determine returned value 
       	 		return self.champ_id  
       	 		
class Champion(models.Model):
	champ_id = models.CharField(max_length=200, default="000")
	name = models.CharField(max_length=200, default="Tweemo")
	icon = models.CharField(max_length=200, default="../icons/champion/Unknown.png")
	def __str__(self):              #to determine returned value 
       	 		return self.champ_id
       	 		
class Version(models.Model):
	region = models.CharField(max_length=200, default="eune")
	version = models.CharField(max_length=200, default="1.0.0")
	def __str__(self):              #to determine returned value 
       	 		return self.region		

       	 		
      	 		
