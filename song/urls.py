from django.urls import path
from song.views import downloaded_song, create_song, song, delete_song

app_name = 'song'

urlpatterns = [
    path('downloaded_song/', downloaded_song, name='downloaded_song'),
    path('create_song/', create_song, name='create_song'),
    path('view/', song, name='song'),
    path('delete_song/', delete_song, name='delete_song')
]