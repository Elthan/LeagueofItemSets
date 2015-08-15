# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0009_auto_20150815_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='champion',
            name='stats',
            field=models.ForeignKey(to='database.ChampionStat', default='000'),
        ),
        migrations.AlterField(
            model_name='championstat',
            name='armor',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='championstat',
            name='armorperlevel',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='championstat',
            name='attackdamage',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='championstat',
            name='attackdamageperlevel',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='championstat',
            name='attackrange',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='championstat',
            name='attackspeedoffset',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='championstat',
            name='attackspeedperlevel',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='championstat',
            name='champ_id',
            field=models.CharField(max_length=200, default='000'),
        ),
        migrations.AlterField(
            model_name='championstat',
            name='crit',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='championstat',
            name='critperlevel',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='championstat',
            name='hp',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='championstat',
            name='hpperlevel',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='championstat',
            name='hpregen',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='championstat',
            name='hpregenperlevel',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='championstat',
            name='movespeed',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='championstat',
            name='mp',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='championstat',
            name='mpperlevel',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='championstat',
            name='mpregen',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='championstat',
            name='mpregenperlevel',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='championstat',
            name='spellblock',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='championstat',
            name='spellblockperlevel',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='FlatArmorMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='FlatAttackSpeedMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='FlatBlockMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='FlatCritChanceMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='FlatCritDamageMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='FlatEXPBonus',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='FlatEnergyPoolMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='FlatEnergyRegenMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='FlatHPPoolMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='FlatHPRegenMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='FlatMPPoolMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='FlatMPRegenMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='FlatMagicDamageMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='FlatMovementSpeedMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='FlatPhysicalDamageMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='FlatSpellBlockMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='PercentArmorMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='PercentAttackSpeedMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='PercentBlockMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='PercentCritChanceMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='PercentCritDamageMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='PercentDodgeMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='PercentEXPBonus',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='PercentHPPoolMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='PercentHPRegenMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='PercentLifeStealMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='PercentMPPoolMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='PercentMPRegenMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='PercentMagicDamageMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='PercentMovementSpeedMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='PercentPhysicalDamageMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='PercentSpellBlockMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='PercentSpellVampMod',
            field=models.DecimalField(max_digits=11, decimal_places=5, default=0),
        ),
    ]
