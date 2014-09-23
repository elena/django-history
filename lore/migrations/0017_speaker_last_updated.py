# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0016_auto_20140921_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 22, 12, 54, 42, 250881), auto_now=True),
            preserve_default=False,
        ),
    ]
