# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20140920_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_end',
            field=models.DateTimeField(null=True, verbose_name='End date/time', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_start',
            field=models.DateTimeField(null=True, verbose_name='Start date/time', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='website',
            field=models.URLField(null=True, verbose_name='Website', blank=True),
        ),
    ]
