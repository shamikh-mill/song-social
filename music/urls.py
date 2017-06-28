from django.conf.urls import url
from . import views # import views from music directory

app_name = 'music'
urlpatterns = [
    # No pattern, goes to home page /music/
    url(r'^$', views.IndexView.as_view(), name = 'index'), # index for each individual app, means nothing after music/ in url

    # /music/<album_id>
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),
    url(r'album/add/$', views.AlbumCreate.as_view(), name = "album-add"),

]
