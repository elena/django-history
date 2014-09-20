# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0006_auto_20140917_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='youtube_thumbnail',
            field=models.URLField(null=True, verbose_name='Youtube thumbnail', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='talk',
            name='abstract',
            field=models.TextField(null=True, verbose_name='Abstract', blank=True),
        ),
        migrations.AlterField(
            model_name='talk',
            name='pyvideo_content',
            field=models.TextField(null=True, verbose_name='PyVideo content', blank=True),
        ),
        migrations.AlterField(
            model_name='talk',
            name='pyvideo_summary',
            field=models.TextField(null=True, verbose_name='PyVideo summary', blank=True),
        ),
        migrations.AlterField(
            model_name='talk',
            name='pyvideo_tags',
            field=models.TextField(null=True, verbose_name='PyVideo tags', blank=True),
        ),
        migrations.AlterField(
            model_name='talk',
            name='speaker_bio',
            field=models.TextField(null=True, verbose_name='Speaker bio', blank=True),
        ),
        migrations.AlterField(
            model_name='talk',
            name='youtube_content',
            field=models.TextField(null=True, verbose_name='Youtube content', blank=True),
        ),
        migrations.AlterField(
            model_name='talk',
            name='youtube_summary',
            field=models.TextField(null=True, verbose_name='Youtube summary', blank=True),
        ),
    ]
