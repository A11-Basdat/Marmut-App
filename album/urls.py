from django.urls import path
from album.views import create_album, album, album_label

app_name = 'album'

urlpatterns = [
    path('create_album/', create_album, name='create_album'),
    path('album/', album, name='album'),
    path('album_label/', album_label, name='album_label'),
]