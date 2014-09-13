from django.contrib import admin

from .models import Series, Event


class EventInlines(admin.TabularInline):
    model = Event


class SeriesAdmin(admin.ModelAdmin):
    model = Series
    inlines = [EventInlines]

admin.site.register(Series, SeriesAdmin)


class EventAdmin(admin.TabularInline):
    model = Event

admin.site.register(Event, EventAdmin)
