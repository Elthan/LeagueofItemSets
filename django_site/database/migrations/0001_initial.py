# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(default='000', max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('gold_total', models.SmallIntegerField()),
                ('gold_base', models.SmallIntegerField()),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerItemSet',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('item_set_id', models.CharField(max_length=200)),
                ('item_set_file', models.FileField(upload_to='')),
                ('item_set_date', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]
