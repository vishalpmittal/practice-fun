from django.shortcuts import render, get_object_or_404
from models import Album, Song


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'vishmusic/index.html', context)


def detail(request, album_id):
    # try:
    #     album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("The Album requested (id = " + album_id + ") does not exit")

    # this replaces all of the code above
    album = get_object_or_404(Album, pk=album_id)

    return render(request, 'vishmusic/album-details.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    print("---1---album:" + str(album))
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'vishmusic/album-details.html', {
            'album': album,
            'error_message': "You did not select a valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'vishmusic/album-details.html', {'album': album})
