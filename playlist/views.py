from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect   
from playlist.forms import PlaylistForm
from playlist.models import Playlist
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection 

def userplaylist(request):
    return render(request, "userplaylist.html")


def addplaylist(request):
    form = PlaylistForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        playlist = form.save(commit=False)
        playlist.user = request.user
        playlist.save()
        return redirect('main:userplaylist')

    context = {'form': form}
    return render(request, "addplaylist.html", context)

def editplaylist(request, id):
    playlist = Playlist.objects.get(pk = id)
    form = PlaylistForm(request.POST or None, instance=playlist)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('playlist:userplaylist'))

    context = {'form': form}
    return render(request, "editplaylist.html", context)

def deleteplaylist(request, id):
    playlist = Playlist.objects.get(pk = id)
    playlist.delete()
    return HttpResponseRedirect(reverse('playlist:userplaylist'))



