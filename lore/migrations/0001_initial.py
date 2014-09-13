# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20140913_1546'),
        ('taggit', '0002_auto_20140913_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, null=True, verbose_name='Title', blank=True)),
                ('colour', models.CharField(help_text=b'Arbitrary colour for presentation', max_length=7, null=True, verbose_name='Color', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=128, null=True, verbose_name='Full name', blank=True)),
                ('prenom', models.CharField(help_text=b'Name for casual reference.', max_length=64, null=True, verbose_name='Prenom', blank=True)),
                ('people', models.CharField(max_length=30, null=True, verbose_name='Django people username', blank=True)),
                ('pyvideo_pk', models.IntegerField(help_text=b'ID number used by PyVideo', null=True, verbose_name='PyVideo pk', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_live', models.BooleanField(default=True, verbose_name='Live')),
                ('date_delivered', models.DateTimeField(help_text=b'The date the talk was actually given/delivered/presented.', verbose_name='Date delivered')),
                ('title', models.CharField(max_length=256, null=True, verbose_name='Title', blank=True)),
                ('abstract', models.TextField(verbose_name='Abstract', blank=True)),
                ('speaker_bio', models.TextField(verbose_name='Speaker bio', blank=True)),
                ('conference_url', models.URLField(null=True, verbose_name=b'PyVideo url', blank=True)),
                ('categories', models.ManyToManyField(help_text=b"Curated and official 'categorisation' eg.: ORM; Optimization.", to='lore.Category')),
                ('event', models.ForeignKey(blank=True, to='events.Event', null=True)),
                ('speakers', models.ManyToManyField(to='lore.Speaker')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
