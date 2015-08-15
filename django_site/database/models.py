from django.db import models

# Create your models here.
class PlayerItemSet(models.Model):
	item_set_id = models.CharField(max_length=200) #or other field
	item_set_file = models.FileField()
	item_set_date = models.DateTimeField('date created')
	def __str__(self):              #to determine returned value 
       	 		return self.item_set_id
       	 		
class Item(models.Model):
	item_id = models.CharField(max_length=200, default="000")
	description = models.CharField(max_length=200)
	gold_total = models.SmallIntegerField()
	gold_base = models.SmallIntegerField()
	on_map = models.CharField(max_length=200, default='all')
	name = models.CharField(max_length=200, default="itemname")
	tags = models.CharField(max_length=200, default=["all", "them", "tags"])
	image = models.CharField(max_length=200, default="some/path.img")
	stacks = models.BooleanField(default=1)
	def __str__(self):              #to determine returned value 
       	 		return self.item_id
       	 		
class ItemStat(models.Model):
	stats_id = models.ForeignKey(Item, default="000") 
	FlatArmorMod = models.DecimalField(max_digits=11, decimal_places=5)
	FlatAttackSpeedMod = models.DecimalField(max_digits=11, decimal_places=5)
	FlatBlockMod = models.DecimalField(max_digits=11, decimal_places=5)
	FlatCritChanceMod = models.DecimalField(max_digits=11, decimal_places=5)
	FlatCritDamageMod = models.DecimalField(max_digits=11, decimal_places=5)
	FlatEXPBonus = models.DecimalField(max_digits=11, decimal_places=5)
	FlatEnergyPoolMod = models.DecimalField(max_digits=11, decimal_places=5)
	FlatEnergyRegenMod = models.DecimalField(max_digits=11, decimal_places=5)
	FlatHPPoolMod = models.DecimalField(max_digits=11, decimal_places=5)
	FlatHPRegenMod = models.DecimalField(max_digits=11, decimal_places=5)
	FlatMPPoolMod = models.DecimalField(max_digits=11, decimal_places=5)
	FlatMPRegenMod = models.DecimalField(max_digits=11, decimal_places=5)
	FlatMagicDamageMod = models.DecimalField(max_digits=11, decimal_places=5)
	FlatMovementSpeedMod = models.DecimalField(max_digits=11, decimal_places=5)
	FlatPhysicalDamageMod = models.DecimalField(max_digits=11, decimal_places=5)
	FlatSpellBlockMod = models.DecimalField(max_digits=11, decimal_places=5)
	PercentArmorMod = models.DecimalField(max_digits=11, decimal_places=5)
	PercentAttackSpeedMod = models.DecimalField(max_digits=11, decimal_places=5)
	PercentBlockMod = models.DecimalField(max_digits=11, decimal_places=5)
	PercentCritChanceMod = models.DecimalField(max_digits=11, decimal_places=5)
	PercentCritDamageMod = models.DecimalField(max_digits=11, decimal_places=5)
	PercentDodgeMod = models.DecimalField(max_digits=11, decimal_places=5)
	PercentEXPBonus = models.DecimalField(max_digits=11, decimal_places=5)	
	PercentHPPoolMod = models.DecimalField(max_digits=11, decimal_places=5)	
	PercentHPRegenMod = models.DecimalField(max_digits=11, decimal_places=5)
	PercentLifeStealMod = models.DecimalField(max_digits=11, decimal_places=5)
	PercentMPPoolMod = models.DecimalField(max_digits=11, decimal_places=5)
	PercentMPRegenMod = models.DecimalField(max_digits=11, decimal_places=5)
	PercentMagicDamageMod = models.DecimalField(max_digits=11, decimal_places=5)
	PercentMovementSpeedMod = models.DecimalField(max_digits=11, decimal_places=5)
	PercentPhysicalDamageMod = models.DecimalField(max_digits=11, decimal_places=5)
	PercentSpellBlockMod = models.DecimalField(max_digits=11, decimal_places=5)
	PercentSpellVampMod = models.DecimalField(max_digits=11, decimal_places=5)	
	def __str__(self):              #to determine returned value 
       	 		return self.item_id
       	 		
      	 		
