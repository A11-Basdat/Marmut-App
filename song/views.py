from django.shortcuts import render, redirect
from song.models import Song
from django.http import HttpResponseRedirect
from django.urls import reverse

def create_song(request):
    return render(request, 'createSong.html')

def song(request):
    return render(request, 'song.html')

def downloaded_song(request):
    return render(request, "downloaded_song.html")

def deletesongfromplaylist(request, id):
    song = Song.objects.get(pk = id)
    song.delete()
    return HttpResponseRedirect(reverse('playlist:userplaylist'))
