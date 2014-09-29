# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20140920_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='google_plus',
            field=models.URLField(null=True, verbose_name='Google +plus url', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='pyvideo_category_pk',
            field=models.IntegerField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='youtube_channel_id',
            field=models.CharField(max_length=32, null=True, verbose_name='Youtube channel id', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='youtube_thumbnail',
            field=models.URLField(null=True, verbose_name='Youtube photo', blank=True),
            preserve_default=True,
        ),
    ]
