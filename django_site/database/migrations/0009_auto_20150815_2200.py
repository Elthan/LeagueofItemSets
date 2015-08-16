# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_auto_20150815_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChampionStat',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('armor', models.DecimalField(max_digits=11, decimal_places=5)),
                ('armorperlevel', models.DecimalField(max_digits=11, decimal_places=5)),
                ('attackdamage', models.DecimalField(max_digits=11, decimal_places=5)),
                ('attackdamageperlevel', models.DecimalField(max_digits=11, decimal_places=5)),
                ('attackrange', models.DecimalField(max_digits=11, decimal_places=5)),
                ('attackspeedoffset', models.DecimalField(max_digits=11, decimal_places=5)),
                ('attackspeedperlevel', models.DecimalField(max_digits=11, decimal_places=5)),
                ('crit', models.DecimalField(max_digits=11, decimal_places=5)),
                ('critperlevel', models.DecimalField(max_digits=11, decimal_places=5)),
                ('hp', models.DecimalField(max_digits=11, decimal_places=5)),
                ('hpperlevel', models.DecimalField(max_digits=11, decimal_places=5)),
                ('hpregen', models.DecimalField(max_digits=11, decimal_places=5)),
                ('hpregenperlevel', models.DecimalField(max_digits=11, decimal_places=5)),
                ('movespeed', models.DecimalField(max_digits=11, decimal_places=5)),
                ('mp', models.DecimalField(max_digits=11, decimal_places=5)),
                ('mpperlevel', models.DecimalField(max_digits=11, decimal_places=5)),
                ('mpregen', models.DecimalField(max_digits=11, decimal_places=5)),
                ('mpregenperlevel', models.DecimalField(max_digits=11, decimal_places=5)),
                ('spellblock', models.DecimalField(max_digits=11, decimal_places=5)),
                ('spellblockperlevel', models.DecimalField(max_digits=11, decimal_places=5)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=200, default='eune')),
                ('version', models.CharField(max_length=200, default='1.0.0')),
            ],
        ),
        migrations.RenameField(
            model_name='itemstat',
            old_name='stats_id',
            new_name='item_id',
        ),
        migrations.AlterField(
            model_name='champion',
            name='icon',
            field=models.CharField(max_length=200, default='../icons/champion/Unknown.png'),
        ),
        migrations.AlterField(
            model_name='item',
            name='icon',
            field=models.CharField(max_length=200, default='../icons/item/3460.png'),
        ),
        migrations.AddField(
            model_name='championstat',
            name='champ_id',
            field=models.ForeignKey(to='database.Champion', default='000'),
        ),
    ]
