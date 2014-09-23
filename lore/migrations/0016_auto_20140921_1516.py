# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0015_auto_20140921_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='people_finding',
            field=models.TextField(null=True, verbose_name='Django people details', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='speaker',
            name='people_photo',
            field=models.URLField(null=True, verbose_name='Django people gravatar', blank=True),
            preserve_default=True,
        ),
    ]
