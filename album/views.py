from django.shortcuts import render, redirect

def create_album(request):
    return render(request, 'createAlbum.html')

def album(request):
    return render(request, 'album.html')

