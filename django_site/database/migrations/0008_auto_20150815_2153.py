# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_auto_20150815_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('champ_id', models.CharField(max_length=200, default='000')),
                ('name', models.CharField(max_length=200, default='Tweemo')),
                ('icon', models.CharField(max_length=200, default='../icons/3460.png')),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
        migrations.AddField(
            model_name='item',
            name='icon',
            field=models.CharField(max_length=200, default='../icons/3460.png'),
        ),
    ]
