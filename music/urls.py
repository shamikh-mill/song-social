from django.conf.urls import url
from . import views # import views from music directory

app_name = 'music'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'), # index for each individual app, means nothing after music/ in url
    # /music/<album_id>
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),
    # /music/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name = "album-add"),
    # /music/album/2
    url(r'album/(?P<pk>[0-9]+)/edit$', views.AlbumUpdate.as_view(), name = 'album-update'),
    # /music/album/2/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name = 'album-delete'),
    # register
    url(r'^register/$', views.UserFormView.as_view(), name = 'register'),

    url(r'song/add/$', views.SongCreate.as_view(), name = "song-add"),
]
