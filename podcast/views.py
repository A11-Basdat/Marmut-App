from django.shortcuts import render

def create_podcast(request):
    return render(request, "createPodcast.html")

def list_podcast(request):
    return render(request, "listPodcast.html")

def create_episode(request):
    return render(request, "createEpisode.html")

def list_episode(request):
    return render(request, "listEpisode.html")
