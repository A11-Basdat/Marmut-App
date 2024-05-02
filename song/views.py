from django.shortcuts import render

# Create your views here.
def downloaded_song(request):
    return render(request, "downloaded_song.html")