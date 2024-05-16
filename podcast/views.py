from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection

def create_podcast(request):
    return render(request, "createPodcast.html")

def list_podcast(request):
    return render(request, "listPodcast.html")

def create_episode(request):
    return render(request, "createEpisode.html")

def list_episode(request):
    return render(request, "listEpisode.html")

def play_podcast(request, podcast_id):
    
    cursor = connection.cursor()
    cursor.execute(f""" 
        SELECT 
        k.judul, 
        g.genre, 
        a.nama, 
        k.durasi, 
        k.tanggal_rilis, 
        k.tahun, 
        de.judul AS episode_judul, 
        de.deskripsi AS episode_deskripsi, 
        de.durasi AS episode_durasi, 
        de.tanggal_rilis AS episode_tanggal_rilis
        FROM 
        podcast AS p
        JOIN konten AS k ON p.id_konten = k.id
        JOIN akun AS a ON p.email_podcaster = a.email
        LEFT JOIN episode AS de ON de.id_konten_podcast = p.id_konten
        JOIN genre AS g ON g.id_konten = p.id_konten
        WHERE 
        p.id_konten = '{podcast_id}';
    """)

    results = cursor.fetchall()
    
    judul, genre, nama, durasi, tanggal_rilis, tahun, *_ = results[0]

    podcast = {
        'judul': judul,
        'genre': genre,
        'nama': nama,
        'durasi': durasi,
        'tanggal_rilis': tanggal_rilis,
        'tahun': tahun,
        'episodes': []
    }

    jam = podcast['durasi']//60
    menit = podcast['durasi']%60

    podcast['durasi'] = f"{jam} Jam {menit} Menit"
    for _, _, _, _, _, _, episode_judul, deskripsi, episode_durasi, episode_tanggal_rilis in results:
        episode = {
            'episode_judul': episode_judul,
            'deskripsi': deskripsi,
            'episode_durasi': episode_durasi,
            'episode_tanggal_rilis': episode_tanggal_rilis
        }
        podcast['episodes'].append(episode)

    return render(request, "detailPodcast.html", podcast)