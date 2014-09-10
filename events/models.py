# -*- coding: utf-8 -*-
from django.db import models


class Series(models.Model):
    name = models.CharField(max_length=64)
    website = models.URLField()


class Event(models.Model):
    series = models.ForeignKey('events.Series', null=True, blank=True)
    series_number = models.CharField(max_length=32, blank=True,
                                     help_text='Example: Year or yyyy-mm-dd')

    name = models.CharField(max_length=64)
    website = models.URLField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    def __str__(self):
        return self.name
