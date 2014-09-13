# -*- coding: utf-8 -*-
from django.conf.urls import include, patterns, url
from lore import views
from lore.views import talk, speaker


urls = patterns('lore.views',
    url(r'^speaker$',
        speaker.ListView.as_view(), name='speaker_list'),
    url(r'^speaker/(?P<slug>\w+)/$',
        speaker.DetailView.as_view(), name='speaker_detail'),
)

urlpatterns = patterns(
    '', (r'^', include(urls, namespace='talks')),
)
