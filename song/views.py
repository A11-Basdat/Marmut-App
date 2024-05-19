from django.shortcuts import render, redirect
from django.db import connection
def create_song(request):
    return render(request, 'createSong.html')

def song(request):
    return render(request, 'song.html')

def downloaded_song(request):
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT k.judul, a.nama
        FROM downloaded_song ds
        JOIN konten k ON ds.id_song = k.id
        JOIN song s ON k.id = s.id_konten
        JOIN artist ar ON s.id_artist = ar.id
        JOIN akun a on a.email = ar.email_akun;
    """)
    results = cursor.fetchall()
    context = {
        'results' : results
    }
    return render(request, "downloaded_song.html", context)
