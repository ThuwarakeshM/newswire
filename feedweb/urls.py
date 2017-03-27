from django.conf.urls import url

from . import views

app_name = 'feedweb'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<lang>\w+)$', views.index, name='index'),
    url(r'^(?P<cat>\w+)$', views.index, name='index'),
    url(r'^(?P<cat>\w+)/(?P<lang>\w+)$', views.index, name='index'),
]
