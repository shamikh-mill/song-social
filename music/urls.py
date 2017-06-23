from django.conf.urls import url
from . import views # import views from music directory

app_name = 'music'
urlpatterns = [
    # No pattern, goes to home page /music/
    url(r'^$', views.index, name = 'index'), # index for each individual app, means nothing after music/ in url

    # /music/<album_id>
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name = 'detail'),

    # /music/<album_id>/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]
