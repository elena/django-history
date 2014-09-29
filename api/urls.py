# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import include, patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import talk


urls = patterns(
    'api.views',

    (r'^$', 'api_root'),

    url(r'^talks/(?P<pk>[0-9]+)$',
        talk.TalkDetailAPI.as_view(), name='talk_api_detail'),
)


urlpatterns = patterns('',
    (r'^', include(urls, namespace='api')),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
