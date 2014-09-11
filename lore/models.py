# -*- coding: utf-8 -*-
from django.db import models
from taggit.managers import TaggableManager
from django.utils.translation import ugettext_lazy as _


class Host(models.Model):
    ## @@ Would ever want to arbitrarily add hosts?
    # There will probably only ever be tiny clearly defined set.
    # Initial list: youtube, pyvideo, soundcloud
    pass


class Talk(models.Model):
    event = models.ForeignKey('events.Event', null=True, blank=True)
    tags = TaggableManager(_('Tags'))
    abstract = models.Textarea(_('Abstract'), blank=True)
    date_delivered = models.DateTimeField(_('Date delivered'))


class Media(models.Model):
    host = models.ForeignKey('lore.Host')
