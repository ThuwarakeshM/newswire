from django.conf.urls import url

from . import views
app_name='NewsFeed'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<feed_id>[0-9]+)/$', views.index, name='index'),
]