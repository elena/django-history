# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import include, patterns, url
from ..views import speaker


urls = patterns('contents.views',

    ## Speakers

    url(r'^speakers/create/$',
        speaker.AddView.as_view(), name='speakers_add'),
)

urlpatterns = patterns('',
    (r'^', include(urls, namespace='talks')),
)
