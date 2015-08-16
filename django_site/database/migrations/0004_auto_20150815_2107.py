# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20150815_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='stacks',
            field=models.BooleanField(default=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=200, default='itemname'),
        ),
    ]
