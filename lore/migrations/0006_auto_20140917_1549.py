# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0005_auto_20140917_0451'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='pyvideo_video_url',
            field=models.URLField(null=True, verbose_name=b'PyVideo hosted url', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='talk',
            name='conference_url',
            field=models.URLField(null=True, verbose_name=b'Conference url', blank=True),
        ),
    ]
