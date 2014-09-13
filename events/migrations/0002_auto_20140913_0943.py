# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='latitude',
            field=models.FloatField(null=True, verbose_name='Latitude', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='location_description',
            field=models.CharField(max_length=50, null=True, verbose_name='Location', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='longitude',
            field=models.FloatField(null=True, verbose_name='Longitude', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='date_end',
            field=models.DateTimeField(verbose_name='End date/time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_start',
            field=models.DateTimeField(verbose_name='Start date/time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(help_text=b'', max_length=64, verbose_name='Event name'),
        ),
        migrations.AlterField(
            model_name='event',
            name='series_number',
            field=models.CharField(help_text=b'Example: Year or yyyy-mm-dd', max_length=32, verbose_name='Series number', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='website',
            field=models.URLField(verbose_name='Website'),
        ),
        migrations.AlterField(
            model_name='series',
            name='name',
            field=models.CharField(help_text=b'eg. DjangoCon Australia', max_length=64, verbose_name='Event name'),
        ),
        migrations.AlterField(
            model_name='series',
            name='website',
            field=models.URLField(verbose_name='Website'),
        ),
    ]
