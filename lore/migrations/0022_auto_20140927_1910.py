# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0021_auto_20140927_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='date_delivered',
            field=models.DateTimeField(help_text=b'The date the talk was actually given/delivered/presented.', null=True, verbose_name='Date delivered', blank=True),
        ),
        migrations.AlterField(
            model_name='talk',
            name='view_count',
            field=models.IntegerField(null=True, verbose_name='View count', blank=True),
        ),
    ]
