import uuid
from datetime import datetime
import random

from django.shortcuts import render, redirect
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from song.forms import *
from django.contrib.auth.decorators import login_required

from base.helper.function import parse
from song.query import *
from urllib.parse import unquote

def song(request):
    album = request.GET.get('album')
    album_name = unquote(album)
    request.session['album_name'] = album_name
    context = {}
    if request.session['is_artist']:
        cursor = connection.cursor()
        query = get_artist_song_query(request.session['email'], request.session['album_name'])
        cursor.execute(query)
        res = parse(cursor)[0]
        for attr in res:
            context[attr] = res[attr]
    elif request.session['is_songwriter']:
        cursor = connection.cursor()
        query = get_songwriter_song_query(request.session['email'], request.session['album_name'])
        cursor.execute(query)
        res = parse(cursor)[0]
        for attr in res:
            context[attr] = res[attr]
    elif request.session['is_label']:
        cursor = connection.cursor()
        query = get_label_song_query(request.session['email'], request.session['album_name'])
        cursor.execute(query)
        res = parse(cursor)[0]
        for attr in res:
            context[attr] = res[attr]
    return render(request, 'song.html', {'context': context, 'album_name': album_name})


@csrf_exempt
def create_song(request):
    if request.session['is_artist']:
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

        form = createSongArtistForm(songwriter, genre, request.POST or None)

        if request.method == 'POST' and 'form_submit' in request.POST and form.is_valid():
            judul_lagu = form.cleaned_data['judul_lagu']
            id_songwriter = form.cleaned_data['daftar_songwriter']
            genre = form.cleaned_data['daftar_genre']
            durasi = form.cleaned_data['durasi']
            id_song = uuid.uuid4()
            date_ymd = datetime.now().strftime('%Y-%m-%d')
            date_y = datetime.now().strftime('%Y')

            query = find_artist_id_hc(request.session['email'])
            cursor = connection.cursor()
            cursor.execute(query)
            res = cursor.fetchone()
            id_artist = res[0]
            id_phc_artist = res[1]

            query = find_album(request.session['album_name'])
            cursor = connection.cursor()
            cursor.execute(query)
            id_album = cursor.fetchone()[0]

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
            return redirect('song:song')

    elif request.session['is_songwriter']:
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

        form = createSongArtistForm(songwriter, genre, request.POST or None)

        if request.method == 'POST' and 'form_submit' in request.POST and form.is_valid():
            judul_lagu = form.cleaned_data['judul_lagu']
            id_songwriter = form.cleaned_data['daftar_songwriter']
            genre = form.cleaned_data['daftar_genre']
            durasi = form.cleaned_data['durasi']
            id_song = uuid.uuid4()
            date_ymd = datetime.now().strftime('%Y-%m-%d')
            date_y = datetime.now().strftime('%Y')

            query = find_artist_id_hc(request.session['email'])
            cursor = connection.cursor()
            cursor.execute(query)
            res = cursor.fetchone()
            id_artist = res[0]
            id_phc_artist = res[1]

            query = find_album(request.session['album_name'])
            cursor = connection.cursor()
            cursor.execute(query)
            id_album = cursor.fetchone()[0]

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
            return redirect('song:song')

    context = {
        'form': form,
    }
    return render(request, 'createSong.html', context)



def downloaded_song(request):
    if 'email' not in request.session:
        return redirect('/authentication/login/')
    
    email = request.session['email']
    cursor = connection.cursor()
    cursor.execute("""
        SELECT COUNT(*) FROM premium WHERE email = %s;
    """, [email])
    premium_count = cursor.fetchone()[0]

    if premium_count == 0:
        context = {
            'is_premium': False
        }
    else:
        cursor.execute("""
            SELECT k.judul, a.nama
            FROM downloaded_song ds
            JOIN konten k ON ds.id_song = k.id
            JOIN song s ON k.id = s.id_konten
            JOIN artist ar ON s.id_artist = ar.id
            JOIN akun a ON a.email = ar.email_akun
            WHERE ds.email_downloader = %s;
        """, [email])
        results = cursor.fetchall()
        context = {
            'results': results,
            'is_premium': True
        }
    return render(request, "downloaded_song.html", context)

def delete_song(request):
    album = request.GET.get('album')
    album_name = unquote(album)
    cursor = connection.cursor()
    query = delete_song_query(album_name)
    cursor.execute(query)
    return redirect('song:song')