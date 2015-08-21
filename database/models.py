from django.db import models
from django.utils import timezone


class PlayerItemSet(models.Model):
        ID = models.CharField(primary_key=True, max_length=50, default="0") #or other field
        Title = models.CharField(max_length=200, default="Made by LoIS")
        Date = models.DateTimeField('date created', default=timezone.now)
        Type = models.CharField(max_length=6, default="custom")
        Map = models.CharField(max_length=3, default="any")
        Mode = models.CharField(max_length=7, default="any")
        Priority = models.BooleanField(default="false")
        SortRank = models.SmallIntegerField(default=0)

        #to determine returned value
        def __str__(self): 
                return str(self.ItemSetID)

        
class Block(models.Model):
        BlockType = models.CharField(max_length=200, default="Custom made")
        RecMath = models.BooleanField(default="false")
        MinSummonerLevel = models.SmallIntegerField(default=-1)
        MaxSummonerLevel = models.SmallIntegerField(default=-1)
        ShowIfSummonerSpell = models.CharField(max_length=50, default="")
        HideIfSummonerSpell = models.CharField(max_length=50, default="")
        PlayerItemSet = models.ForeignKey(PlayerItemSet)

        def __str_(self):
                return self.Type

        
class BlockItem(models.Model):
        ItemID = models.IntegerField(default=0)
        Count = models.IntegerField(default=1)
        Block = models.ForeignKey(Block)
        
        # to determine return value
        def __str__(self):
                return str(self.ItemID)

        
class ItemStat(models.Model):
        ItemID = models.IntegerField(primary_key=True, default=0)
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

        #to determine returned value 
        def __str__(self):
                return str(self.ItemID)
        
        
class Item(models.Model):
        ItemID = models.IntegerField(primary_key=True, default=0)
        Description = models.CharField(max_length=200, default="Describe me!")
        GoldTotal = models.SmallIntegerField(default=0)
        GoldBase = models.SmallIntegerField(default=0)
        Name = models.CharField(max_length=200, default="item_name")
        Tags = models.CharField(max_length=200, default=["all", "them", "tags"])
        Icon = models.CharField(max_length=200, default="database/static/icons/item/3460.png")
        Stacks = models.IntegerField(default=1)
        Into = models.CharField(max_length=200, default=[""])
        Purchasable = models.BooleanField(default=False)
        
        #to determine returned value 
        def __str__(self): 
                return self.Name
        
        
class ChampionStat(models.Model):
        ChampID = models.IntegerField(primary_key=True, default=0) 
        Armor = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        ArmorPerLevel = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        AttackDamage = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        AttackDamagePerLevel = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        AttackRange = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        AttackSpeedOffset = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        AttackSpeedPerLevel = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        Crit = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        CritPerLevel = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        HP = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        HPPerLevel = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        HPRegen = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        HPRegenPerLevel = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        MoveSpeed = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        MP = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        MPPerLevel = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        MPRegen = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        MPRegenPerLevel = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        SpellBlock = models.DecimalField(max_digits=11, decimal_places=5, default=0)
        SpellBlockPerLevel = models.DecimalField(max_digits=11, decimal_places=5, default=0)        

        #to determine returned value 
        def __str__(self):
                return str(self.ChampID)

        
class Champion(models.Model):
        ChampID = models.IntegerField(primary_key=True, default=0)
        Name = models.CharField(max_length=200, default="Tweemo")
        Icon = models.CharField(max_length=200, default="icons/champion/Unknown.png")

        #to determine returned value 
        def __str__(self):
                return self.Name
        
class Version(models.Model):
        Region = models.CharField(primary_key=True, max_length=200, default="eune")
        Version = models.CharField(max_length=200, default="1.0.0")

        #to determine returned value 
        def __str__(self): 
                return self.Version
