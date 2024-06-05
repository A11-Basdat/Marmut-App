from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db import connection, DatabaseError
from django.urls import reverse
from .query import get_podcast_query
from .format import format_podcast_data
import uuid
from datetime import datetime

def create_podcast(request):
    email = request.session['email']
    cursor = connection.cursor()

    cursor.execute(f"""
        SELECT DISTINCT genre
        FROM GENRE;
    """)

    results = cursor.fetchall()
    
    genres = {
        'genres': [
        {
            'genre': result[0]
        }
        for result in results
        ]
    }

    print(genres)


    if request.method == 'POST':
        judul = request.POST.get('judul')
        genre = request.POST.get('genre')
        # durasi = request.POST.get('durasi')

        new_uuid = str(uuid.uuid4())
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime('%Y-%m-%d')
        current_year = current_datetime.year

        cursor.execute(f"""
            INSERT INTO KONTEN 
            VALUES ('{new_uuid}', '{judul}', '{formatted_date}', '{current_year}', '0');
        """)

        cursor.execute(f"""
            INSERT INTO GENRE VALUES 
            ('{new_uuid}', '{genre}');  
        """)

        cursor.execute(f"""
            INSERT INTO PODCAST  VALUES 
            ('{new_uuid}', '{email}');
        """)

        cursor.execute(f"""
            SELECT KONTEN.judul, GENRE.genre, KONTEN.durasi 
            FROM KONTEN, GENRE 
            WHERE KONTEN.id='{new_uuid}' AND GENRE.id_konten=KONTEN.id;
        """)
        create_result = cursor.fetchone()

        
        context = {
            'judul': create_result[0],
            'genre': create_result[1],
            'durasi': create_result[2],
            'error': None
        }

        return redirect('podcast:list_podcast')

    return render(request, "createPodcast.html", genres)

def list_podcast(request):
    cursor = connection.cursor()
    email = request.session['email']
    cursor.execute(f"""
                SELECT k.judul, k.durasi, k.id, COUNT(e.id_konten_podcast) AS episode_count
                FROM podcast AS p
                JOIN konten AS k ON p.id_konten = k.id
                LEFT JOIN episode AS e ON e.id_konten_podcast = p.id_konten
                WHERE p.email_podcaster = '{email}'
                GROUP BY k.judul, k.durasi, k.id;
            """)
    
    results = cursor.fetchall()
    podcasts = [
        {
            'id': result[2],
            'judul': result[0],
            'durasi': result[1],
            'jumlah_episode': result[3],
        }
        for result in results
    ]

    context = {
        'podcasts': podcasts,
    }

    return render(request, "listPodcast.html", context)

def create_episode(request, podcast_id):
    cursor = connection.cursor()

    if request.method == 'POST':
        judul = request.POST.get('judul')
        deskripsi = request.POST.get('deskripsi')
        durasi = request.POST.get('durasi')

        new_uuid = str(uuid.uuid4())
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime('%Y-%m-%d')

        cursor.execute(f"""
            INSERT INTO EPISODE 
            VALUES ('{new_uuid}','{podcast_id}', '{judul}', '{deskripsi}', '{durasi}', '{formatted_date}');
        """)

        return redirect(reverse('podcast:list_episode', args=[podcast_id]))

    cursor.execute(f"""
            SELECT k.judul
            FROM KONTEN as k, PODCAST as p
            WHERE P.id_konten = k.id and P.id_konten = '{podcast_id}';
    """)

    result = cursor.fetchall()[0][0]
    context = {
        'podcast_id': podcast_id,
        'judul' : result
    }

    return render(request, "createEpisode.html", context)

def list_episode(request, podcast_id):
    cursor = connection.cursor()
    cursor.execute(f"""
                SELECT e.judul, e.deskripsi, e.durasi, e.tanggal_rilis, e.id_episode, k.judul AS podcast_judul
                FROM podcast AS p
                JOIN konten AS k ON k.id = p.id_konten
                LEFT JOIN episode AS e ON e.id_konten_podcast = p.id_konten
                WHERE p.id_konten = '{podcast_id}';
            """)
    
    results = cursor.fetchall()
    print(results)

    podcast_dict = {
        'judul_podcast': results[0][5] if results else '',
        'episodes': []
    }

    if results[0][0]:
        for episode in results:
            episode_dict = {
                'judul': episode[0],
                'deskripsi': episode[1],
                'durasi': episode[2],
                'tanggal_rilis': episode[3],  
                'id_episode': str(episode[4]) 
            }
            podcast_dict['episodes'].append(episode_dict)


    return render(request, "listEpisode.html", podcast_dict)

def play_podcast(request, podcast_id):
    cursor = connection.cursor()
    cursor.execute(get_podcast_query(podcast_id))

    results = cursor.fetchall()
    print(results)
    podcast = format_podcast_data(results)
    print(podcast)

    return render(request, "detailPodcast.html", podcast)

def delete_episode(request, episode_id):
    cursor = connection.cursor()

    cursor.execute(f"""
                SELECT id_konten_podcast
                FROM EPISODE
                WHERE id_episode = '{episode_id}';
            """)
    results = cursor.fetchall()

    cursor.execute(f"""
                DELETE
                FROM EPISODE
                WHERE id_episode = '{episode_id}';
            """)
    
    return redirect(reverse('podcast:list_episode', args=[str(results[0][0])]))

def delete_podcast(request, podcast_id):
    cursor = connection.cursor()
    cursor.execute(f"""
                DELETE
                FROM KONTEN
                WHERE id = '{podcast_id}';
            """)
    
    return redirect(reverse('podcast:list_podcast'))