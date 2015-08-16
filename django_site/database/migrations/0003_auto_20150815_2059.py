# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20150815_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.CharField(default='some/path.img', max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='tags',
            field=models.CharField(default=['all', 'them', 'tags'], max_length=200),
        ),
    ]
