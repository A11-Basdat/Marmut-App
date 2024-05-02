from django.urls import path
from song.views import create_song, song

app_name = 'song'

urlpatterns = [
    path('create_song/', create_song, name='create_song'),
    path('song/', song, name='song'),
]