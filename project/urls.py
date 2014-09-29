# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
from lore.views import HomePageView


urlpatterns = patterns(
    '',

    # Home
    url(r'^$', HomePageView.as_view(), name='home'),

    # Talks
    (r'^talks/', include('lore.urls')),

    # Events
    (r'^events/', include('events.urls')),

    # Content
    (r'^content/', include('contents.urls')),

    # API
    (r'^api/', include('api.urls')),

    # Django Admin
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # Only serve media files if in a development environment
    from django.conf.urls.static import static
    from django.views.generic import TemplateView
    MEDIA_ROOT = getattr(settings, 'MEDIA_ROOT')
    MEDIA_URL = getattr(settings, 'MEDIA_URL').lstrip('/')

    urlpatterns = urlpatterns + patterns('',
        (r'^errors/404$', TemplateView.as_view(template_name='404.html')),
        (r'^errors/500$', TemplateView.as_view(template_name='500.html')),
        # (r'^%(media_url)s(?P<path>.*)$' %(
        #   {'media_url': re.escape(MEDIA_URL)}),
        #   'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
