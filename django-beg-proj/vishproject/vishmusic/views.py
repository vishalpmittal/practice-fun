from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album, Song
from django.core.urlresolvers import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'vishmusic/index.html'
    context_object_name = 'all_albums_list'

    def get_queryset(self):
        return Album.objects.all()


class DetailsView(generic.DetailView):
    model = Album
    template_name = 'vishmusic/album-details.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('vishmusic:index')