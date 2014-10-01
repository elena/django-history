# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0022_auto_20140927_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='categories',
            field=models.ManyToManyField(help_text=b"Curated and official 'categorisation' eg.: ORM; Optimization.", to=b'lore.Category', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='talk',
            name='speakers',
            field=models.ManyToManyField(to=b'lore.Speaker', null=True, blank=True),
        ),
    ]
