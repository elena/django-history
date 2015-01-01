# -*- coding: utf-8 -*-
from django.conf.urls import include, patterns, url
from django.contrib import admin

from events.views import event, series


urls = patterns('events.views',

    url(r'^(?P<slug>[\w-]+)$',
        event.DetailView.as_view(), name='event_detail'),

    url(r'^$',
        event.ListView.as_view(), name='event_list'),

    url(r'^series$',
        series.ListView.as_view(), name='series_list'),
    url(r'^series/(?P<slug>[\w-]+)$',
        series.DetailView.as_view(), name='series_detail'),
)

urlpatterns = patterns(
    '', (r'^', include(urls, namespace='events')),
)
