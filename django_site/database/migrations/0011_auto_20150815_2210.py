# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_auto_20150815_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='stats',
            field=models.ForeignKey(default='000', to='database.ItemStat'),
        ),
        migrations.AlterField(
            model_name='itemstat',
            name='item_id',
            field=models.CharField(max_length=200, default='000'),
        ),
    ]
