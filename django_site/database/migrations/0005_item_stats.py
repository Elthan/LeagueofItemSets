# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20150815_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='stats',
            field=models.ForeignKey(to='database.PlayerItemSet', default='5465153'),
        ),
    ]
