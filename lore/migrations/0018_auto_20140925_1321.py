# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0017_speaker_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='slug',
            field=models.SlugField(max_length=64, null=True, blank=True),
        ),
    ]
