from django.shortcuts import render
from django.utils import timezone

from .models import FeedCategory, Feed, Section, FeedLanguage


def home(request):
    return index(request, lang='EN', cat=0, feedid=0)


def categoryView(request, cat):
    lang = FeedCategory.objects.get(pk=cat).feed_category_lang.feed_language_code
    return index(request, cat=cat, lang=lang, feedid=0)


def langView(request, lang):
    return index(request, lang=lang, cat=0, feedid=0)


def feedView(request, feedid):
    lang = Feed.objects.get(pk=feedid).feed_language.feed_language_code
    return index(request, lang=lang, cat=0, feedid=feedid)


def index(request, lang, cat, feedid):
    categories = FeedCategory.objects.filter(feed_category_lang__feed_language_code=lang)
    if feedid:
        feed = Feed.objects.get(pk=feedid)
        feeds = Feed.objects.filter(feed_category_id=feed.feed_category.id, feed_language_id=feed.feed_language.id)[:5]
    elif cat:
        feeds = Feed.objects.filter(feed_category_id=cat, feed_language__feed_language_code=lang)[
                :5]
        feed = feeds[0]
    else:
        feeds = Feed.objects.filter(feed_language__feed_language_code=lang)[:5]
        feed = feeds[0]

    feed_sections = Section.objects.filter(feed_id=feed.id)
    languages = FeedLanguage.objects.all()

    context = {
        'categories': categories,
        'feeds': feeds,
        'feed': feed,
        'feed_sections': feed_sections,
        'languages': languages,
    }
    return render(request, 'feedweb/index.html', context)
