# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0002_auto_20140913_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talk',
            name='youtube_url',
        ),
        migrations.AddField(
            model_name='talk',
            name='youtube_id',
            field=models.CharField(max_length=32, null=True, verbose_name=b'Youtube id', blank=True),
            preserve_default=True,
        ),
    ]
