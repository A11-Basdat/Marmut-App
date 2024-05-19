import random
from datetime import datetime
import uuid

from django.shortcuts import render, redirect
from django.db import connection
from django.views.decorators.csrf import csrf_exempt

from base.helper.function import parse
from album.query import *
from album.forms import *

def album(request):
    context = {}
    if request.session['is_label']:
        cursor = connection.cursor()
        query = get_label_album_query(request.session['email'])
        cursor.execute(query)
        res = parse(cursor)[0]
        for attr in res:
            context[attr] = res[attr]
    elif request.session['is_artist']:
        cursor = connection.cursor()
        query = get_artist_album_query(request.session['email'])
        cursor.execute(query)
        res = parse(cursor)[0]
        for attr in res:
            context[attr] = res[attr]
    elif request.session['is_songwriter']:
        cursor = connection.cursor()
        query = get_songwriter_album_query(request.session['email'])
        cursor.execute(query)
        res = parse(cursor)[0]
        for attr in res:
            context[attr] = res[attr]
    return render(request, 'album.html', context)

@csrf_exempt
def create_album(request):
    if request.session['is_artist']:
        query = label_find_query()
        cursor = connection.cursor()
        cursor.execute(query)
        res = parse(cursor)
        label = [(label['id'], label['nama']) for label in res]

        query = songwriter_find_query()
        cursor = connection.cursor()
        cursor.execute(query)
        res = parse(cursor)
        songwriter = [(songwriter['id'], songwriter['nama']) for songwriter in res]

        query = genre_find_query()
        cursor = connection.cursor()
        cursor.execute(query)
        res = parse(cursor)
        genre = [(genre['genre'], genre['genre']) for genre in res]

        form = createAlbumArtistForm(label, songwriter, genre, request.POST or None)

        if request.method == 'POST' and 'form_submit' in request.POST and form.is_valid():
            judul_album = form.cleaned_data['judul_album']
            id_label = form.cleaned_data['daftar_label']
            judul_lagu = form.cleaned_data['judul_lagu']
            id_songwriter = form.cleaned_data['daftar_songwriter']
            genre = form.cleaned_data['daftar_genre']
            durasi = form.cleaned_data['durasi']
            id_album = uuid.uuid4()
            id_song = uuid.uuid4()
            date_ymd = datetime.now().strftime('%Y-%m-%d')
            date_y = datetime.now().strftime('%Y')

            query = find_artist_id_hc(request.session['email'])
            cursor = connection.cursor()
            cursor.execute(query)
            res = cursor.fetchone()
            id_artist = res[0]
            id_phc_artist = res[1]


            query = insert_album_query(id_album, judul_album, 1, id_label, durasi)
            cursor.execute(query)
            query = insert_konten_query(id_song, judul_lagu, date_ymd, date_y, durasi)
            cursor.execute(query)
            query = insert_song_query(id_song, id_artist, id_album, 0, 0)
            cursor.execute(query)
            query = insert_royalti_query(id_phc_artist, id_song, random.randint(20000,60000))
            cursor.execute(query)
            query = insert_genre_query(id_song, genre)
            cursor.execute(query)
            query = insert_songwriter_write_song_query(id_songwriter, id_song)
            cursor.execute(query)
            return redirect('album:album')

    elif request.session['is_songwriter']:
        query = label_find_query()
        cursor = connection.cursor()
        cursor.execute(query)
        res = parse(cursor)
        label = [(label['id'], label['nama']) for label in res]

        query = artist_find_query()
        cursor = connection.cursor()
        cursor.execute(query)
        res = parse(cursor)
        artist = [(artist['id'], artist['nama']) for artist in res]

        query = genre_find_query()
        cursor = connection.cursor()
        cursor.execute(query)
        res = parse(cursor)
        genre = [(genre['genre'], genre['genre']) for genre in res]

        form = createAlbumSongwriterForm(label, artist, genre, request.POST or None)

        if request.method == 'POST' and 'form_submit' in request.POST and form.is_valid():
            judul_album = form.cleaned_data['judul_album']
            id_label = form.cleaned_data['daftar_label']
            judul_lagu = form.cleaned_data['judul_lagu']
            id_artist = form.cleaned_data['daftar_artist']
            genre = form.cleaned_data['daftar_genre']
            durasi = form.cleaned_data['durasi']
            id_album = uuid.uuid4()
            id_song = uuid.uuid4()
            date_ymd = datetime.now().strftime('%Y-%m-%d')
            date_y = datetime.now().strftime('%Y')

            query = find_songwriter_id_hc(request.session['email'])
            cursor = connection.cursor()
            cursor.execute(query)
            res = cursor.fetchone()
            id_songwriter = res[0]
            id_phc_songwriter = res[1]

            query = insert_album_query(id_album, judul_album, 1, id_label, durasi)
            cursor.execute(query)
            query = insert_konten_query(id_song, judul_lagu, date_ymd, date_y, durasi)
            cursor.execute(query)
            query = insert_song_query(id_song, id_artist, id_album, 0, 0)
            cursor.execute(query)
            query = insert_royalti_query(id_phc_songwriter, id_song, random.randint(2,6))
            cursor.execute(query)
            query = insert_genre_query(id_song, genre)
            cursor.execute(query)
            query = insert_songwriter_write_song_query(id_songwriter, id_song)
            cursor.execute(query)
            return redirect('album:album')

    context = {
        'form': form,
    }
    return render(request, 'createAlbum.html', context)




