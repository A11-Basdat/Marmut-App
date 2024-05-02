from django.shortcuts import render

def create_podcast(request):
    return render(request, "createPodcast.html")
