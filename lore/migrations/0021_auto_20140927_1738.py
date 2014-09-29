# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0020_speaker_github'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speaker',
            options={'ordering': ['full_name']},
        ),
    ]
