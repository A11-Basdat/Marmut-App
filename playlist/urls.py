from django.urls import path
from playlist.views import userplaylist, addplaylist, editplaylist

app_name = 'playlist'

urlpatterns = [
    path('', userplaylist, name='userplaylist'),
    path('addplaylist', addplaylist, name='addplaylist'),
    path('addplaylist/<int:id>', addplaylist, name='addplaylist'),
]
