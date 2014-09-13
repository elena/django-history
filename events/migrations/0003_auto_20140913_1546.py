# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20140913_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='colour',
            field=models.CharField(help_text=b'Arbitrary colour for presentation', max_length=7, null=True, verbose_name='Color', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='is_live',
            field=models.BooleanField(default=True, verbose_name='Live'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(help_text=b'Example: DjangoCon AU 2014', max_length=64, verbose_name='Event name'),
        ),
    ]
