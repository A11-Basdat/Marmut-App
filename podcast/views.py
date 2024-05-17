from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection, DatabaseError
from .query import get_podcast_query
from .format import format_podcast_data
import uuid
from datetime import datetime

def create_podcast(request):
    cursor = connection.cursor()

    if request.method == 'POST':
        judul = request.POST.get('judul')
        genre = request.POST.get('genre')
        durasi = request.POST.get('durasi')

        new_uuid = str(uuid.uuid4())
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime('%Y-%m-%d')
        current_year = current_datetime.year

        try: 
            cursor.execute(f"""
                INSERT INTO KONTEN 
                VALUES ('{new_uuid}', '{judul}', '{formatted_date}', '{current_year}', '{durasi}');
            """)

            cursor.execute(f"""
                INSERT INTO GENRE VALUES 
                ('{new_uuid}', '{genre}');
            """)

            cursor.execute(f"""
                INSERT INTO PODCAST VALUES 
                ('{new_uuid}', 'laisha07@example.net');
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

        except DatabaseError as e:
            # Handle database errors
            context = {
                'judul': None,
                'genre': None,
                'durasi': None,
                'error': str(e)
            }

        return render(request, "createPodcast.html", context)
        
        


    return render(request, "createPodcast.html")

def list_podcast(request):
    return render(request, "listPodcast.html")

def create_episode(request):
    return render(request, "createEpisode.html")

def list_episode(request):
    return render(request, "listEpisode.html")

def play_podcast(request, podcast_id):
    cursor = connection.cursor()
    cursor.execute(get_podcast_query(podcast_id))

    results = cursor.fetchall()
    podcast = format_podcast_data(results)

    return render(request, "detailPodcast.html", podcast)