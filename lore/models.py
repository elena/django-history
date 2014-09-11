# -*- coding: utf-8 -*-
from django.db import models
from taggit.managers import TaggableManager
from django.utils.translation import ugettext_lazy as _


class Talk(models.Model):
    event = models.ForeignKey('events.Event', null=True, blank=True)
    tags = TaggableManager(_('Tags'))
