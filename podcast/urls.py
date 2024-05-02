from django.urls import path
from podcast.views import create_podcast, list_podcast

app_name = 'podcast'

urlpatterns = [
    path('create/', create_podcast, name='create_podcast'),
    path('all-podcast/', list_podcast, name='list_podcast'),
]

