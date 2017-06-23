from .models import Album, Song
from django.shortcuts import render, get_object_or_404

# views take requests and sends back an HTTP response.


def index(request): # always pass in a request
    all_albums = Album.objects.all() # store results of database API call
     # django will look into templates directory for this music/index file.
    return render(request, 'music/index.html', {'all_albums': all_albums}) # always pass in request

def detail(request, album_id): # album_id is passed in with URL request! Call this from urls.py with views.detail.
    # return HttpResponse("<h2>Details for album id: " + str(album_id) + "<h2>")
    album = get_object_or_404(Album, pk = album_id)
    return render(request, 'music/detail.html', {'album': album})  # always pass in request

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk = request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "You did not select a valid song!",
        })
    else:
        selected_song.is_favorite = True # make it a fave
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})  # redirects to the same page!
