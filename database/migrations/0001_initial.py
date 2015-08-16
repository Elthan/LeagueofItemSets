# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('champ_id', models.IntegerField(default=0)),
                ('name', models.CharField(default='Tweemo', max_length=200)),
                ('icon', models.CharField(default='icons/champion/Unknown.png', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ChampionStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('champ_id', models.IntegerField(default=0)),
                ('armor', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('armor_per_level', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('attack_damage', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('attack_damage_per_level', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('attack_range', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('attack_speed_offset', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('attack_speed_per_level', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('crit', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('crit_per_level', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('hp', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('hp_per_level', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('hp_regen', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('hp_regen_per_level', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('move_speed', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('mp', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('mp_per_level', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('mp_regen', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('mp_regen_per_level', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('spell_block', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('spell_block_per_level', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('item_id', models.IntegerField(default=0)),
                ('description', models.CharField(default='Describe me!', max_length=200)),
                ('gold_total', models.SmallIntegerField(default=0)),
                ('gold_base', models.SmallIntegerField(default=0)),
                ('on_map', models.CharField(default='all', max_length=200)),
                ('name', models.CharField(default='item_name', max_length=200)),
                ('tags', models.CharField(default=['all', 'them', 'tags'], max_length=200)),
                ('icon', models.CharField(default='../icons/item/3460.png', max_length=200)),
                ('stacks', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ItemStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('item_id', models.IntegerField(default=0)),
                ('flat_armor_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('flat_attack_speed_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('flat_block_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('flat_crit_chance_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('flat_crit_damage_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('flat_exp_bonus', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('flat_energy_pool_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('flat_energy_regen_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('flat_hp_pool_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('flat_hp_regen_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('flat_mp_pool_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('flat_mp_regen_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('flat_magic_damage_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('flat_movement_speed_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('flat_physical_damage_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('flat_spell_block_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('percent_armor_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('percent_attack_speed_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('percent_block_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('percent_crit_chance_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('percent_crit_damage_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('percent_dodge_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('percent_exp_bonus', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('percent_hp_pool_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('percent_hp_regen_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('percent_life_steal_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('percent_mp_pool_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('percent_mp_regen_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('percent_magic_damage_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('percent_movement_speed_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('percent_physical_damage_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('percent_spell_block_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
                ('percent_spell_vamp_mod', models.DecimalField(default=0, max_digits=11, decimal_places=5)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerItemSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('item_set_id', models.CharField(default='000', max_length=200)),
                ('item_set_file', models.FileField(default='', upload_to='')),
                ('item_set_date', models.DateTimeField(verbose_name='date created', default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('region', models.CharField(default='eune', max_length=200)),
                ('version', models.CharField(default='1.0.0', max_length=200)),
            ],
        ),
    ]
