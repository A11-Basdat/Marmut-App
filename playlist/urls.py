from django.urls import path
from playlist.views import userplaylist
from playlist.views import addplaylist

app_name = 'playlist'

urlpatterns = [
    path('', userplaylist, name='userplaylist'),
    path('addplaylist', addplaylist, name='addplaylist'),
]
