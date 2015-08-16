# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='on_map',
            field=models.CharField(default='all', max_length=200),
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.CharField(default='', max_length=200),
        ),
    ]
