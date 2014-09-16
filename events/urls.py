# -*- coding: utf-8 -*-
from django.conf.urls import include, patterns, url
from django.contrib import admin

from events.views import event, series


urls = patterns('events.views',

    url(r'^$',
        event.ListView.as_view(), name='event_list'),
    url(r'^(?P<slug>\w+)$',
        event.DetailView.as_view(), name='event_detail'),
)

urlpatterns = patterns(
    '', (r'^', include(urls, namespace='events')),
)
