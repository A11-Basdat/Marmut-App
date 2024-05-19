from django.shortcuts import render, redirect
from django.db import connection
from base.helper.function import parse
from dashboard.query import *

def dashboard(request):
    context = {}
    if request.session['is_label']:
        cursor = connection.cursor()
        query = get_label_detail_query(request.session['email'])
        cursor.execute(query)
        res = parse(cursor)[0]
        for attr in res:
            context[attr] = res[attr]
    elif request.session['is_podcaster']:
        cursor = connection.cursor()
        query = get_podcaster_detail_query(request.session['email'])
        cursor.execute(query)
        res = parse(cursor)[0]
        for attr in res:
            context[attr] = res[attr]
    elif request.session['is_artist']:
        cursor = connection.cursor()
        query = get_artist_detail_query(request.session['email'])
        cursor.execute(query)
        res = parse(cursor)[0]
        for attr in res:
            context[attr] = res[attr]
    elif request.session['is_songwriter']:
        cursor = connection.cursor()
        query = get_songwriter_detail_query(request.session['email'])
        cursor.execute(query)
        res = parse(cursor)[0]
        for attr in res:
            context[attr] = res[attr]
    elif request.session['is_penggunabiasa']:
        cursor = connection.cursor()
        query = get_penggunabiasa_detail_query(request.session['email'])
        cursor.execute(query)
        res = parse(cursor)[0]
        for attr in res:
            context[attr] = res[attr]

    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT k.judul, k.durasi, k.id
        FROM KONTEN as k, PODCAST as p
        WHERE k.id = p.id_konten
    """)

    res = cursor.fetchall()

    podcast_list = [{
    'title': title,
    'duration': duration,
    'id': str(id)
    } for title, duration, id in res]

    context['all_podcasts'] = podcast_list

    print(context)

    return render(request, 'dashboard.html', context)

def search_bar(request):
    query = request.GET.get('query', '')

    if query:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT 'Podcast' as tipe, k.judul, a.nama
            FROM podcast p
            JOIN konten k ON p.id_konten = k.id
            JOIN podcaster po ON po.email = p.email_podcaster
            JOIN akun a ON po.email = a.email
            WHERE k.judul ILIKE %s OR a.nama ILIKE %s
            UNION ALL
            SELECT 'Song' as tipe, k.judul, a.nama
            FROM song s
            JOIN konten k ON s.id_konten = k.id
            JOIN artist ar ON s.id_artist = ar.id
            JOIN akun a ON ar.email_akun = a.email
            WHERE k.judul ILIKE %s OR a.nama ILIKE %s
            UNION ALL
            SELECT 'User Playlist' as tipe, up.judul, a.nama
            FROM user_playlist up
            JOIN akun a ON up.email_pembuat = a.email
            WHERE up.judul ILIKE %s OR a.nama ILIKE %s
        """, [f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%'])

        results = cursor.fetchall()
        podcasts = [result for result in results if result[0] == 'Podcast']
        songs = [result for result in results if result[0] == 'Song']
        user_playlists = [result for result in results if result[0] == 'User Playlist']
    else:
        podcasts, songs, user_playlists = [], [], []

    context = {
        'query': query,
        'podcasts': podcasts,
        'songs': songs,
        'user_playlists': user_playlists,
    }
    return render(request, 'search_bar.html', context)
