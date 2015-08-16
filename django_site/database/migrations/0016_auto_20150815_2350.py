# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0015_auto_20150815_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='champion',
            name='stats',
        ),
        migrations.RemoveField(
            model_name='item',
            name='stats',
        ),
    ]
