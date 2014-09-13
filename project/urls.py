# -*- coding: utf-8 -*-
from django.conf.urls import include, patterns
from django.contrib import admin


urls = patterns('',

    # Events
    (r'^events/', include('events.urls')),


    # Django Admin
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
