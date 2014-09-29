# -*- coding: utf-8 -*-
from django.conf.urls import include, patterns, url
from .views import talk, speaker


urls = patterns('lore.views',

    url(r'^$',
        talk.ListView.as_view(), name='talk_list'),

    url(r'^(?P<event_slug>[-_\w]+)/(?P<slug>[-_\w]+)$',
        talk.DetailView.as_view(), name='talk_detail'),
    url(r'^(?P<slug>[-_\w]+)$',
        talk.DetailView.as_view(), name='talk_detail'),

    url(r'^speaker$',
        speaker.ListView.as_view(), name='speaker_list'),
    url(r'^speaker/(?P<slug>\w+)/$',
        speaker.DetailView.as_view(), name='speaker_detail'),
)

urlpatterns = patterns(
    '', (r'^', include(urls, namespace='talks')),
)
