# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0011_auto_20150815_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(default='Describe me!', max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='gold_base',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='gold_total',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='playeritemset',
            name='item_set_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 15, 22, 13, 47, 253449, tzinfo=utc), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='playeritemset',
            name='item_set_file',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='playeritemset',
            name='item_set_id',
            field=models.CharField(default='000', max_length=200),
        ),
    ]
