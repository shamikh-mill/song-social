from django.db import models
from django.core.urlresolvers import reverse


# Create your models here. Blueprint for database- how are we sorting data for our app?
class Album(models.Model): # all classes have to inherit from this
    artist = models.CharField(max_length=250) # going to be a column in our database!
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs = {'pk' : self.pk})

    def __str__(self): # gives string representation of the object!
        return self.album_title + ' - ' + self.artist

class Song(models.Model): # songs need to be a part of an album.
    album = models.ForeignKey(Album, on_delete= models.CASCADE) # assigns song to album with a unique ID, the foreignkey.
    # when album is deleted, also delete the songs. Each album can be a set that we can add songs to.
    file_type = models.CharField(max_length = 10)
    song_title = models.CharField(max_length= 250)
    is_favorite = models.BooleanField(default= False)

    def __str__(self):
        return self.song_title
