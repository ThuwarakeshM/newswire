from django.contrib import admin

from .models import *


# Register your models here.
class SectionInline(admin.StackedInline):
    model = Section
    extra = 1


class FeedAdmin(admin.ModelAdmin):
    fields = ['title', 'feed_category', 'feed_language']
    inlines = [SectionInline]


admin.site.register(Feed, FeedAdmin)
admin.site.register(FeedCategory)
admin.site.register(FeedLanguage)

