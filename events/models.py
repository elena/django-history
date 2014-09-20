# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


class Series(models.Model):
    """ Series is just nice for convenience. As it is not a compulsory field
    against a talk, it isn't to be taken too seriously.
    """

    name = models.CharField(_('Event name'),
                            max_length=64,
                            help_text="eg. DjangoCon Australia")
    website = models.URLField(_('Website'))
    slug = models.SlugField(max_length=64)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('events:series_detail', kwargs={'slug': self.slug})


class Event(models.Model):
    is_live = models.BooleanField(_('Live'), default=True)
    colour = models.CharField(_('Color'), max_length=7, null=True, blank=True,
                              help_text = "Arbitrary colour for presentation")

    series = models.ForeignKey('events.Series', null=True, blank=True)
    series_number = models.CharField(_('Series number'),
                                     max_length=32,
                                     blank=True,
                                     help_text='Example: Year or yyyy-mm-dd')

    name = models.CharField(_('Event name'),
                            max_length=64,
                            help_text='Example: DjangoCon AU 2014')
    slug = models.SlugField(max_length=64)

    pyvideo_category_title = models.CharField(max_length=128,
                                              null=True, blank=True)

    website = models.URLField(_('Website'))
    date_start = models.DateTimeField(_('Start date/time'))
    date_end = models.DateTimeField(_('End date/time'))

    latitude = models.FloatField(_('Latitude'), null=True, blank=True)
    longitude = models.FloatField(_('Longitude'), null=True, blank=True)
    location_description = models.CharField(_('Location'), max_length=50,
                                            null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('events:event_detail', kwargs={'slug': self.slug})

    @property
    def latitude_str(self):
        return str(self.latitude)

    @property
    def longitude_str(self):
        return str(self.longitude)
