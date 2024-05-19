from django.shortcuts import render, redirect
from django.db import connection
from django.contrib.auth.decorators import login_required

def create_song(request):
    return render(request, 'createSong.html')

def song(request):
    return render(request, 'song.html')

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
