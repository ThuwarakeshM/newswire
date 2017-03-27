from django.shortcuts import render

from .models import FeedCategory, Feed, Section


def index(request, lang='TA', cat=0):
    categories = FeedCategory.objects.filter(feed_category_lang__feed_language_code=lang)
    if cat:
        feeds = Feed.objects.filter(feed_category=cat, feed_language__feed_language_code=lang)[:5]
    else:
        feeds = Feed.objects.filter(feed_language__feed_language_code=lang)[:5]
    feed = feeds[0]

    feed_sections = Section.objects.filter(feed_id=feed.id)

    context = {
        'categories': categories,
        'feeds': feeds,
        'feed': feed,
        'feed_sections': feed_sections,
    }
    return render(request, 'feedweb/index.html', context)
