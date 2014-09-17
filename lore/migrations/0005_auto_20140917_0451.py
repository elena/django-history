# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0004_auto_20140916_0453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talk',
            name='pyvideo_url',
        ),
        migrations.AddField(
            model_name='talk',
            name='pyvideo_pk',
            field=models.IntegerField(null=True, verbose_name=b'PyVideo pk', blank=True),
            preserve_default=True,
        ),
    ]
