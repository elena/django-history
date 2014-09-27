# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0019_talk_youtube_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='github',
            field=models.CharField(max_length=64, null=True, verbose_name='Github username', blank=True),
            preserve_default=True,
        ),
    ]
