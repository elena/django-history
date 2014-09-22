# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_pyvideo_category_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name_plural': 'Series'},
        ),
    ]
