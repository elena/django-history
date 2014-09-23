# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0009_auto_20140920_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='full_name',
            field=models.CharField(max_length=128, verbose_name='Full name'),
        ),
    ]
