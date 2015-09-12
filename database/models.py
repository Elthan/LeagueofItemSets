from django.db import models
from django.utils import timezone


class PlayerItemSet(models.Model):
        ID = models.CharField(primary_key=True, max_length=50, default="0") #or other field
        Title = models.CharField(max_length=200, default="Made by LoIS")
        Date = models.DateTimeField('date created', default=timezone.now)
        Map = models.CharField(max_length=3, default="any")
        Mode = models.CharField(max_length=7, default="any")
        SortRank = models.SmallIntegerField(default=0)

        #to determine returned value
        def __str__(self):
                return str(self.ID)


class Block(models.Model):
        BlockType = models.CharField(max_length=200, default="Custom made")
        RecMath = models.CharField(max_length=10, default="false")
        MinSummonerLevel = models.SmallIntegerField(default=-1)
        MaxSummonerLevel = models.SmallIntegerField(default=-1)
        ShowIfSummonerSpell = models.CharField(max_length=50, default="")
        HideIfSummonerSpell = models.CharField(max_length=50, default="")
        PlayerItemSet = models.ForeignKey(PlayerItemSet)

        def __str_(self):
                return self.BlockType


class BlockItem(models.Model):
        ItemID = models.IntegerField(default=0)
        Count = models.IntegerField(default=1)
        Block = models.ForeignKey(Block)

        # to determine return value
        def __str__(self):
                return str(self.ItemID)


class Item(models.Model):
        ItemID = models.IntegerField(primary_key=True, default=0)
        Description = models.CharField(max_length=200, default="Describe me!")
        GoldTotal = models.SmallIntegerField(default=0)
        GoldBase = models.SmallIntegerField(default=0)
        Name = models.CharField(max_length=200, default="item_name")
        Tags = models.CharField(max_length=200, default=[""])
        Icon = models.CharField(max_length=200, default="http://ddragon.leagueoflegends.com/cdn/5.17.1/img/champion/1001.png")
        Stacks = models.IntegerField(default=1)
        Into = models.CharField(max_length=200, default=[""])
        Purchasable = models.BooleanField(default=False)

        #to determine returned value
        def __str__(self):
                return self.Name


class ItemStat(models.Model):
        ItemID = models.OneToOneField(Item, primary_key=True)
        FlatArmorMod = models.FloatField(null=True, blank=True)
        FlatAttackSpeedMod = models.FloatField(null=True, blank=True)
        FlatBlockMod = models.FloatField(null=True, blank=True)
        FlatCritChanceMod = models.FloatField(null=True, blank=True)
        FlatCritDamageMod = models.FloatField(null=True, blank=True)
        FlatExpBonus = models.FloatField(null=True, blank=True)
        FlatEnergyPoolMod = models.FloatField(null=True, blank=True)
        FlatEnergyRegenMod = models.FloatField(null=True, blank=True)
        FlatHPPoolMod = models.FloatField(null=True, blank=True)
        FlatHPRegenMod = models.FloatField(null=True, blank=True)
        FlatMPPoolMod = models.FloatField(null=True, blank=True)
        FlatMPRegenMod = models.FloatField(null=True, blank=True)
        FlatMagicDamageMod = models.FloatField(null=True, blank=True)
        FlatMovementSpeedMod = models.FloatField(null=True, blank=True)
        FlatPhysicalDamageMod = models.FloatField(null=True, blank=True)
        FlatSpellBlockMod = models.FloatField(null=True, blank=True)
        PercentArmorMod = models.FloatField(null=True, blank=True)
        PercentAttackSpeedMod = models.FloatField(null=True, blank=True)
        PercentBlockMod = models.FloatField(null=True, blank=True)
        PercentCritChanceMod = models.FloatField(null=True, blank=True)
        PercentCritDamageMod = models.FloatField(null=True, blank=True)
        PercentDodgeMod = models.FloatField(null=True, blank=True)
        PercentExpBonus = models.FloatField(null=True, blank=True)
        PercentHPPoolMod = models.FloatField(null=True, blank=True)
        PercentHPRegenMod = models.FloatField(null=True, blank=True)
        PercentLifeStealMod = models.FloatField(null=True, blank=True)
        PercentMPPoolMod = models.FloatField(null=True, blank=True)
        PercentMPRegenMod = models.FloatField(null=True, blank=True)
        PercentMagicDamageMod = models.FloatField(null=True, blank=True)
        PercentMovementSpeedMod = models.FloatField(null=True, blank=True)
        PercentPhysicalDamageMod = models.FloatField(null=True, blank=True)
        PercentSpellBlockMod = models.FloatField(null=True, blank=True)
        PercentSpellVampMod = models.FloatField(null=True, blank=True)
        BaseHPRegenMod = models.FloatField(null=True, blank=True)
        BaseMPRegenMod = models.FloatField(null=True, blank=True)

        #to determine returned value
        def __str__(self):
                return str(self.ItemID)


class Champion(models.Model):
        ChampID = models.IntegerField(primary_key=True, default=0)
        Name = models.CharField(max_length=200, default="All")
        Key = models.CharField(max_length=200, default="All")
        Icon = models.CharField(max_length=200, default="http://ddragon.leagueoflegends.com/cdn/5.17.1/img/champion/Teemo.png")
        Tags = models.CharField(max_length=200, default="");

        #to determine returned value
        def __str__(self):
                return self.Name


class ChampionStat(models.Model):
        ChampID = models.OneToOneField(Champion, primary_key=True)
        Armor = models.FloatField(null=True, blank=True)
        ArmorPerLevel = models.FloatField(null=True, blank=True)
        AttackDamage = models.FloatField(null=True, blank=True)
        AttackDamagePerLevel = models.FloatField(null=True, blank=True)
        AttackRange = models.FloatField(null=True, blank=True)
        AttackSpeedOffset = models.FloatField(null=True, blank=True)
        AttackSpeedPerLevel = models.FloatField(null=True, blank=True)
        Crit = models.FloatField(null=True, blank=True)
        CritPerLevel = models.FloatField(null=True, blank=True)
        HP = models.FloatField(null=True, blank=True)
        HPPerLevel = models.FloatField(null=True, blank=True)
        HPRegen = models.FloatField(null=True, blank=True)
        HPRegenPerLevel = models.FloatField(null=True, blank=True)
        MoveSpeed = models.FloatField(null=True, blank=True)
        MP = models.FloatField(null=True, blank=True)
        MPPerLevel = models.FloatField(null=True, blank=True)
        MPRegen = models.FloatField(null=True, blank=True)
        MPRegenPerLevel = models.FloatField(null=True, blank=True)
        SpellBlock = models.FloatField(null=True, blank=True)
        SpellBlockPerLevel = models.FloatField(null=True, blank=True)

        #to determine returned value
        def __str__(self):
                return str(self.ChampID)


class Version(models.Model):
        Region = models.CharField(primary_key=True, max_length=10, default="eune")
        Version = models.CharField(max_length=20, default="1.0.0")

        #to determine returned value
        def __str__(self):
                return self.Version
