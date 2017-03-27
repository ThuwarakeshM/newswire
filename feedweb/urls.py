from django.conf.urls import url

from . import views

app_name = 'feedweb'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^lang/(?P<lang>\w+)$', views.langView, name='LangView'),
    url(r'^cat/(?P<cat>[0-9]+)$', views.categoryView, name='CatView'),
    url(r'^(?P<feedid>[0-9]+)$', views.feedView, name='FeedView'),
]
