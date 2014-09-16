# -*- coding: utf-8 -*-
from django.db import models
from taggit.managers import TaggableManager
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(_('Title'), max_length=256, null=True, blank=True)
    colour = models.CharField(_('Color'), max_length=7, null=True, blank=True,
                              help_text = "Arbitrary colour for presentation")
    slug = models.SlugField(max_length=64)

    def __str__(self):
        return self.name


class Talk(models.Model):
    is_live = models.BooleanField(_("Live"), default=True)
    event = models.ForeignKey('events.Event', null=True, blank=True)
    speakers = models.ManyToManyField('lore.Speaker')
    tags = TaggableManager(_('Tags'))
    slug = models.SlugField(max_length=64)


    categories = models.ManyToManyField('lore.Category',
                                      help_text="Curated and official 'categorisation' eg.: ORM; Optimization.")

    date_delivered = models.DateTimeField(_('Date delivered'),
                                          help_text="The date the talk was actually given/delivered/presented.")

    """ Detail from conference website """
    title = models.CharField(_('Title'), max_length=256, null=True, blank=True)
    abstract = models.TextField(_('Abstract'), blank=True)
    speaker_bio = models.TextField(_('Speaker bio'), blank=True)
    conference_url = models.URLField('PyVideo url', null=True, blank=True)


    def __str__(self):
        return self.title

    # """ Detail from PyVideo """
    pyvideo_title = models.TextField(_('PyVideo title'), max_length=256,
                                     null=True, blank=True)
    pyvideo_summary = models.TextField(_('PyVideo summary'), blank=True)
    pyvideo_content = models.TextField(_('PyVideo content'), blank=True)
    pyvideo_tags = models.TextField(_('PyVideo content'), blank=True)
    pyvideo_url = models.URLField('PyVideo url', null=True, blank=True)

    # """ Detail from Youtube """
    youtube_id = models.CharField('Youtube id', max_length=32,
                                  null=True, blank=True)
    youtube_title = models.TextField(_('Youtube title'), max_length=256,
                                     null=True, blank=True)
    youtube_summary = models.TextField(_('Youtube summary'), blank=True)
    youtube_content = models.TextField(_('Youtube content'), blank=True)
    youtube_views = models.IntegerField('Youtube views', null=True, blank=True)

    objects = querysets.TalkManager()

class Speaker(models.Model):
    """ There should nearly certainly should be a separate module for speakers.

    But not looking to replace any existing resources out there, just point to them.
    """
    full_name = models.CharField(_('Full name'), max_length=128,
                                 blank=True, null=True)
    prenom = models.CharField(_('Prenom'), max_length=64, blank=True, null=True,
                              help_text="Name for casual reference.")
    people = models.CharField(_('Django people username'), max_length=30,
                              blank=True, null=True)
    pyvideo_pk = models.IntegerField(_('PyVideo pk'), blank=True, null=True,
                                     help_text="ID number used by PyVideo")
    slug = models.SlugField(max_length=64)

    def __str__(self):
        if self.people:
            return "{0} ({1})".format(self.full_name, self.people)
        return self.full_name
