from django.views import generic
from .models import Album, Song
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login # takes user and password and verifies login, gives session ID
from django.views.generic import View
from .forms import UserForm
from django.core.urlresolvers import reverse_lazy

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    # attributes we need from the user
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class SongCreate(CreateView):
    model = Song
    # attributes we need from the user
    fields = ['album', 'file_type', 'song_title']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index') #redirect to here after delete

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'
    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit = False) # not saved to db yet
            # clean (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save() # save to db

            user = authenticate(username = username, password = password) # verify user in db

            if user is not None:
                if user.is_active:
                    login(request, user)
                     # redirect to homepage after login:
                    return redirect('music:index')

            return render(request, self.template_name, {'form': form})
