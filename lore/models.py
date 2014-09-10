# -*- coding: utf-8 -*-
from django.db import models
from taggit.managers import TaggableManager


class Talk(models.Model):
    event = models.ForeignKey('events.Event', null=True, blank=True)
    tags = TaggableManager()
