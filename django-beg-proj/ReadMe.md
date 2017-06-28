Python Django beginners project
===============================

Reference
---------

I have created the contents of this projct while watching the web tutorials on python django
by "thenewboston" (Bucky Roberts) @ following url:

https://www.youtube.com/watch?v=qgGIqRFvFFk&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK&index=1

Env Setup
---------
-  Install homebrew on mac
```
   https://brew.sh/

   /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

-  Install Python
```
   $ brew install python
   $ python --version
   Python 2.7.13
```

-  Install pip:

   -  pip is already installed if you're using Python 2 >=2.7.9 or Python 3 >=3.4
   -  Else refer following link to install pip
   https://pip.pypa.io/en/stable/installing/
```
   $ pip --version
   pip 9.0.1 from /usr/local/lib/python2.7/site-packages (python 2.7)
```

-  Install virtualenv
```
   $ cd django-beg-proj
   $ pip install virtualenv
   $ virtualenv --version
   15.1.0
```

-  Create project and activate virtualenv
```
  $ which python
   /usr/local/bin/python

   $ virtualenv -p /usr/local/bin/python vijango

   $ . vijango/bin/activate
   (vijango) vishalm-m01:django-beg-proj vishalm$ pip isntall django
```

-  Install django
```
   $ . vijango/bin/activate
   (vijango) vishalm-m01:django-beg-proj vishalm$ pip isntall django

   (vijango) vishalm-m01:django-beg-proj vishalm$ python
   Python 2.7.13 (default, Apr  4 2017, 08:46:44)

   >>> import django

   >>> django.VERSION
   (1, 11, 2, u'final', 0)

   control + d

   (vijango) vishalm-m01:django-beg-proj vishalm$ deactivate
```

Django Cheatsheet
-----------------

-  Start and run project
   ```
      django-admin startproject vishproject

      python manage.py runserver
   ```

-  Sync DB with django models
   ```
      python manage.py makemigrations vishmusic
      python manage.py sqlmigrate vishmusic 0001
      python manage.py migrate
   ```

-  Database APIs n filters
   ```
      python manage.py shell
      >>> from vishmusic.models import Album, Song
      >>> Album.objects.all()
   ```
   Create and save objects 1
   ```
      >>> a = Album(artist="t1_artist", album_title="t1_albumtitle", genre="t1_genre", \
                      album_logo="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png")
      >>> a.save()
      >>> Album.objects.all()
      >>> a.artist
      >>> a.id
      >>> a.pk
   ```

   Create and save objects 2
   ```
      >>> b = Album()
      >>> b.artist="t2_artist"
      >>> b.album_title="t2_albumtitle"
      >>> b.genre="t2_genre"
      >>> b.album_logo="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png"
      >>> b.save()

      >>> Album.objects.filter(id=1)
      >>> Album.objects.filter(id=2)
      >>> Album.objects.filter(artist__startswith='t1')
   ```

   Create and save objects FK 1
   ```
      >>> album1 = Album.objects.get(pk=1)
      >>> song1 = Song()
      >>> song1.album = album1
      >>> song1.file_type = 'mp3'
      >>> song1.song_title = 't1_song_title'
      >>> song.save()
   ```

   Create and save objects FK 2
   ```
      >>> album1.song_set.all()
      <QuerySet [<Song: t1_song_title.mp3>]>
      >>>
      >>> album1.song_set.create(song_title='t2_song_title', file_type='mp3')
      <Song: t2_song_title.mp3>
   ```

   Aggregate functions
   ```
   >>> album1.song_set.count()
   2
   ```

-  Django admin

   Enable access
   ```
      $ python manage.py createsuperuser
      Username (leave blank to use 'vishalm'): admin
      Email address: admin@vishproject.com
      Password:
      Password (again): vishpass
      Superuser created successfully. vishpass
   ```

   Register Model for admin access
   -  in <app_folder> -> admin.py -> admin.site.register(Album)

