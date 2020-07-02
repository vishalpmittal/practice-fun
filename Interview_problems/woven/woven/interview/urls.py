from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'inbox/flat', views.flat_inbox, name='flat_inbox'),
    url(r'inbox/threaded', views.threaded_inbox, name='threaded_inbox'),
    url(r'home', views.index, name='index'),
]
