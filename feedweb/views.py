from django.shortcuts import render, get_object_or_404

from .models import FeedCategory, Feed, Section


def index(request, feed_id=0, lang="TA", category=0):
    categories = FeedCategory.objects.filter(feed_category_lang__feed_language_code=lang)
    latest_feeds = Feed.objects.all().order_by('-pub_date')[:5]
    if (feed_id):
        feed = get_object_or_404(Feed, pk=feed_id)
        feed_Sections = Section.objects.filter(feed_id=feed_id)
    else:
        feed = 0
        feed_Sections = 0

    context = {

        'feed': feed,
        'feed_sections': feed_Sections,
        'categories': categories,
        'latest_feeds': latest_feeds,
    }
    return render(request, 'feedweb/index.html', context)
