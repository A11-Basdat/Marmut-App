from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from .query import get_podcast_query
from .format import format_podcast_data

def create_podcast(request):
    return render(request, "createPodcast.html")

def list_podcast(request):
    return render(request, "listPodcast.html")

def create_episode(request):
    return render(request, "createEpisode.html")

def list_episode(request):
    return render(request, "listEpisode.html")

def play_podcast(request, podcast_id):
    cursor = connection.cursor()
    cursor.execute(get_podcast_query(podcast_id))

    results = cursor.fetchall()
    podcast = format_podcast_data(results)

    return render(request, "detailPodcast.html", podcast)