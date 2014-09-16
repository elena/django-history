from django.contrib import admin

from .models import Category, Talk, Speaker


class TalkAdmin(admin.ModelAdmin):
    model = Talk
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Talk, TalkAdmin)


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {"slug":("name",)}

admin.site.register(Category, CategoryAdmin)


class SpeakerAdmin(admin.ModelAdmin):
    model = Speaker
    prepopulated_fields = {"slug":("pk", "full_name",)}

admin.site.register(Speaker, SpeakerAdmin)
