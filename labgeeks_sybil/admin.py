from django.contrib import admin
from labgeeks_sybil.models import Screenshot, Tag


class ScreenshotAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'date', )
    readonly_fields = ('user', 'date', )

admin.site.register(Screenshot, ScreenshotAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(Tag, TagAdmin)
