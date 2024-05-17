from django.shortcuts import render, redirect

def create_song(request):
    return render(request, 'createSong.html')

def song(request):
    return render(request, 'song.html')

def downloaded_song(request):
    return render(request, "downloaded_song.html")
