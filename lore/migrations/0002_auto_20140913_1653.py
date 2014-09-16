# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='pyvideo_content',
            field=models.TextField(default='', verbose_name='PyVideo content', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='talk',
            name='pyvideo_summary',
            field=models.TextField(default='', verbose_name='PyVideo summary', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='talk',
            name='pyvideo_tags',
            field=models.TextField(default='', verbose_name='PyVideo content', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='talk',
            name='pyvideo_title',
            field=models.TextField(max_length=256, null=True, verbose_name='PyVideo title', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='talk',
            name='pyvideo_url',
            field=models.URLField(null=True, verbose_name=b'PyVideo url', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='talk',
            name='youtube_content',
            field=models.TextField(default='', verbose_name='Youtube content', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='talk',
            name='youtube_summary',
            field=models.TextField(default='', verbose_name='Youtube summary', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='talk',
            name='youtube_title',
            field=models.TextField(max_length=256, null=True, verbose_name='Youtube title', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='talk',
            name='youtube_url',
            field=models.URLField(null=True, verbose_name=b'Youtube url', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='talk',
            name='youtube_views',
            field=models.IntegerField(null=True, verbose_name=b'Youtube views', blank=True),
            preserve_default=True,
        ),
    ]
