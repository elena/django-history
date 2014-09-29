# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import include, patterns, url
from rest_framework.urlpatterns import format_suffix_patterns


urls = patterns(
    'api.views',

    (r'^$', 'api_root'),
)


urlpatterns = patterns('',
    (r'^', include(urls, namespace='api')),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
