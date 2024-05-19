from django.urls import path
from playlist.views import userplaylist, addplaylist, editplaylist, deleteplaylist

app_name = 'playlist'

urlpatterns = [
    path('', userplaylist, name='userplaylist'),
    path('addplaylist', addplaylist, name='addplaylist'),
    path('editplaylist/<int:id>', editplaylist, name='editplaylist'),
    path('delete/<int:id>', deleteplaylist, name='deleteplaylist'),
]
