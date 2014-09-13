# -*- coding: utf-8 -*-
from django.db import models
from taggit.managers import TaggableManager
from django.utils.translation import ugettext_lazy as _




class Talk(models.Model):
    is_live = models.BooleanField(_("Live"), default=True)
    event = models.ForeignKey('events.Event', null=True, blank=True)
    tags = TaggableManager(_('Tags'))
    abstract = models.Textarea(_('Abstract'), blank=True)
    date_delivered = models.DateTimeField(_('Date delivered'))


class Media(models.Model):
    host = models.ForeignKey('lore.Host')
