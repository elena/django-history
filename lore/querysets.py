# -*- coding: utf-8 -*-
from django.db import models


class TalkManager(models.Manager):
    """Customised queryset for :py:class:`~lore.models.Talk` model. """

    def get_queryset(self):
        return super(TalkManager, self).get_queryset()

    def popular(self):
        """Filter for talks which are uber-popular.

        :returns: Filtered queryset.
        :rtype: :py:class:`.TalkQuerySet`
        """
        # add from 'Important' tag.
        return self.order_by('-youtube_views')

    def recent(self):
        """Filter for recent talks.

        :returns: Filtered queryset.
        :rtype: :py:class:`.TalkQuerySet`
        """
        return self.order_by('-date_delivered')

    def unwatched(self):
        """Filter for talks which don't have many views.

        :returns: Filtered queryset.
        :rtype: :py:class:`.TalkQuerySet`
        """
        return self.order_by('youtube_views')
