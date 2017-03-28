from django.db import models
from smart_selects.db_fields import ChainedForeignKey


# Create your models here.
class FeedLanguage(models.Model):
    feed_language_code = models.CharField(max_length=4, unique=True)
    feed_language_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.feed_language_code


class FeedCategory(models.Model):
    class Meta:
        unique_together = (('feed_category_name', 'feed_category_lang'),)

    feed_category_name = models.CharField(max_length=20)
    feed_category_lang = models.ForeignKey(FeedLanguage, on_delete=models.CASCADE)

    def __str__(self):
        return self.feed_category_name + " " +self.feed_category_lang.feed_language_code


class Feed(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField('pub_date', auto_now_add=True)
    feed_language = models.ForeignKey(FeedLanguage, on_delete=models.CASCADE)
    # feed_category = models.ForeignKey(FeedCategory, on_delete=models.CASCADE)
    feed_category = ChainedForeignKey(FeedCategory, chained_field="feed_language", chained_model_field="feed_category_lang", show_all=False, auto_choose=True, sort=True)

    def __str__(self):
        return self.title


class Section(models.Model):
    section_title = models.CharField(max_length=250, blank=True)
    section_body = models.TextField(max_length=5000, blank=True)
    section_video_url = models.URLField(max_length=2000, blank=True)
    section_image = models.ImageField(upload_to='img/%Y/%m/%d', blank=True)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
