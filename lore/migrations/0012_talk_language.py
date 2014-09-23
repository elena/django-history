# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0011_talk_pyvideo_copyright'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='language',
            field=models.TextField(null=True, verbose_name='Language', blank=True),
            preserve_default=True,
        ),
    ]
