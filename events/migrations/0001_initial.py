# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('series_number', models.CharField(help_text=b'Example: Year', max_length=32, blank=True)),
                ('name', models.CharField(max_length=64)),
                ('website', models.URLField()),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('website', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='series',
            field=models.ForeignKey(blank=True, to='events.Series', null=True),
            preserve_default=True,
        ),
    ]
