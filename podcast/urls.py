from django.urls import path
from podcast.views import create_episode, create_podcast, list_episode, list_podcast

app_name = 'podcast'

urlpatterns = [
    path('create-podcast/', create_podcast, name='create_podcast'),
    path('all-podcast/', list_podcast, name='list_podcast'),
    path('create-episode/', create_episode, name='create_episode'),
    path('all-episode/', list_episode, name='list_episode'),
]

