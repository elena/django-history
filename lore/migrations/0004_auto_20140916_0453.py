# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0003_auto_20140914_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speaker',
            name='slug',
            field=models.SlugField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='talk',
            name='slug',
            field=models.SlugField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
