# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0012_talk_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='pyvideo_source_url',
            field=models.URLField(null=True, verbose_name='PyVideo source url', blank=True),
            preserve_default=True,
        ),
    ]
