# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0012_auto_20150815_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playeritemset',
            name='item_set_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 8, 15, 22, 17, 39, 498907, tzinfo=utc)),
        ),
    ]
