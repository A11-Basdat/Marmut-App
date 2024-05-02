from django.urls import path
from album.views import create_album, album

app_name = 'album'

urlpatterns = [
    path('create_album/', create_album, name='create_album'),
    path('album/', album, name='album'),
]