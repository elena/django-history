from django.contrib import admin

from .models import Series, Event


class EventInlines(admin.TabularInline):
    model = Event


class SeriesAdmin(admin.ModelAdmin):
    model = Series
    inlines = [EventInlines]
    prepopulated_fields = {"slug":("name",)}

admin.site.register(Series, SeriesAdmin)


class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ['name', 'colour', 'pyvideo_category_pk',
                    'pyvideo_category_title',
                    'youtube_channel_id', 'google_plus', 'website']
    list_editable = ['pyvideo_category_title', 'youtube_channel_id']
    prepopulated_fields = {"slug":("name",)}

admin.site.register(Event, EventAdmin)
