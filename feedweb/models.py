import datetime

from django.db import models

# Create your models here.

class FeedCategory(models.Model):
    feed_category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.feed_category_name


class FeedLanguage(models.Model):
    feed_language_code = models.CharField(max_length=2)

    def __str__(self):
        return self.feed_language_code


class Feed(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField('pub_date', auto_now_add=True)
    feed_category = models.ForeignKey(FeedCategory, on_delete=models.CASCADE)
    feed_language = models.ForeignKey(FeedLanguage, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Section(models.Model):
    section_title = models.CharField(max_length=250, blank=True)
    section_body = models.TextField(max_length=5000, blank=True)
    section_video_url = models.URLField(max_length=2000, blank=True)
    section_image = models.ImageField(upload_to='uploads/%Y/%m/%d/images')
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
