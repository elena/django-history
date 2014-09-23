# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0014_talk_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='youtube_channel_id',
            field=models.CharField(max_length=32, null=True, verbose_name='Youtube channel id', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='talk',
            name='youtube_copyright',
            field=models.CharField(max_length=256, null=True, verbose_name='Youtube copyright', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='talk',
            name='youtube_duration',
            field=models.IntegerField(null=True, verbose_name='Youtube duration', blank=True),
            preserve_default=True,
        ),
    ]
