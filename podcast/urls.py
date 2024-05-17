from django.urls import path
from podcast.views import create_episode, create_podcast, list_episode, list_podcast, play_podcast, delete_episode

app_name = 'podcast'

urlpatterns = [
    path('create-podcast/', create_podcast, name='create_podcast'),
    path('all-podcast/', list_podcast, name='list_podcast'),
    path('delete-episode/<uuid:episode_id>', delete_episode, name='delete_episode'),
    path('create-episode/<uuid:podcast_id>/', create_episode, name='create_episode'),
    path('all-episode/<uuid:podcast_id>/', list_episode, name='list_episode'),
    path('play/<uuid:podcast_id>/', play_podcast, name='play_podcast'),
]

