from django.contrib import admin

from .models import Category, Talk, Speaker


class TalkAdmin(admin.ModelAdmin):
    model = Talk
    list_display = ['event', 'title', 'pyvideo_pk', 'youtube_id', 'slug',
                    'pyvideo_video_url', 'pyvideo_source_url']
    list_editable = ['title']
    list_filter = ['event', 'speakers']
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Talk, TalkAdmin)

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['name', 'colour', 'slug']
    list_editable = ['colour']
    prepopulated_fields = {"slug":("name",)}

admin.site.register(Category, CategoryAdmin)


class SpeakerAdmin(admin.ModelAdmin):
    model = Speaker
    prepopulated_fields = {"slug":("full_name",)}

    def __init__(self, *args, **kwargs):
        super(SpeakerAdmin, self).__init__(*args, **kwargs)
        self.list_display = ['full_name', self.display_pyvideo,
                             self.display_people, self.display_finding,
                             self.display_photo]

    def display_pyvideo(self, obj):
        if obj.pyvideo_pk:
            return '<a href="{0}" target="_blank">{1}</a>'.format(
                obj.get_pyvideo_url(), obj.pyvideo_pk)
        else: return ''
    display_pyvideo.allow_tags = True
    display_pyvideo.short_description = 'PyVideo pk'

    def display_people(self, obj):
        if obj.people:
            return '<a href="{0}" target="_blank">{1}</a>'.format(
                obj.get_people_url(), obj.people)
        else: return ''
    display_people.allow_tags = True
    display_people.short_description = 'DjangoPeople'

    def display_finding(self, obj):
        if obj.people:
            return obj.people_finding
        else: return ''
    display_finding.allow_tags = True
    display_finding.short_description = 'Details'

    def display_photo(self, obj):
        if obj.people_photo:
            return '<img src="{0}" width=50>'.format(obj.people_photo)
    display_photo.allow_tags = True
    display_photo.short_description = 'Photo'


admin.site.register(Speaker, SpeakerAdmin)
