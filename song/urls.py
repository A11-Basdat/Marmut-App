from django.urls import path
from song.views import downloaded_song

app_name = 'song'

urlpatterns = [
    path('downloaded_song/', downloaded_song, name='downloaded_song')
]