from django.urls import path
from album.views import create_album, album, delete_album

app_name = 'album'

urlpatterns = [
    path('create_album/', create_album, name='create_album'),
    path('album/', album, name='album'),
    path('delete_album/', delete_album, name='delete_album')
]