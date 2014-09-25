# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0018_auto_20140925_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='youtube_likes',
            field=models.IntegerField(null=True, verbose_name='Youtube likes', blank=True),
            preserve_default=True,
        ),
    ]
