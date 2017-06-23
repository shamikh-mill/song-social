from django.contrib import admin
from .models import Album, Song # .models is models file in current directory

# Register your models here.

admin.site.register(Album)
admin.site.register(Song)