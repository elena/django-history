# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Series(models.Model):
    name = models.CharField(_('Event name'),
                            max_length=64,
                            help_text="eg. DjangoCon Australia")
    website = models.URLField(_('Website'))


class Event(models.Model):
    series = models.ForeignKey('events.Series', null=True, blank=True)
    series_number = models.CharField(_('Series number'),
                                     max_length=32,
                                     blank=True,
                                     help_text='Example: Year or yyyy-mm-dd')

    name = models.CharField(_('Event name'),
                            max_length=64,
                            help_text="")
    website = models.URLField(_('Website'))
    date_start = models.DateTimeField(_('Start date/time'))
    date_end = models.DateTimeField(_('End date/time'))

    def __str__(self):
        return self.name
