# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0007_auto_20140920_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='pyvideo_pk',
            field=models.IntegerField(unique=True, null=True, verbose_name='PyVideo pk', blank=True),
        ),
        migrations.AlterField(
            model_name='talk',
            name='youtube_id',
            field=models.CharField(max_length=32, unique=True, null=True, verbose_name='Youtube id', blank=True),
        ),
    ]
