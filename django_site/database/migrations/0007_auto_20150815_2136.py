# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_itemstat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='stats',
        ),
        migrations.RemoveField(
            model_name='itemstat',
            name='item_id',
        ),
        migrations.AddField(
            model_name='itemstat',
            name='stats_id',
            field=models.ForeignKey(default='000', to='database.Item'),
        ),
    ]
