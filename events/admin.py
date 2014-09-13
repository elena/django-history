from django.contrib import admin

from .models import Series, Event


class SeriesAdmin(admin.ModelAdmin):
    model = Series

admin.site.register(Series, SeriesAdmin)


class EventAdmin(admin.TabularInline):
    model = Event

admin.site.register(Event, EventAdmin)
