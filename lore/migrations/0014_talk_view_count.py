# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0013_talk_pyvideo_source_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='View count'),
            preserve_default=False,
        ),
    ]
