# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0010_auto_20140920_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='pyvideo_copyright',
            field=models.CharField(max_length=256, null=True, verbose_name='PyVideo copyright', blank=True),
            preserve_default=True,
        ),
    ]
