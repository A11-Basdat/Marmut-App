from django.shortcuts import render
from django.db import connection

def list_chart(request):
    cursor = connection.cursor()
    cursor.execute(f"""
            SELECT c.tipe, c.id_playlist
            FROM chart as c;
    """)
    results = cursor.fetchall()
    podcast_list = {'charts':[{'title': title, 'id': str(uuid)} for title, uuid in results]}

    return render(request, "listChart.html", podcast_list)

def detail_chart(request, chart_id):
    cursor = connection.cursor()
    cursor.execute(f"""
            SELECT 
                c.tipe,
                k.judul, 
                ak.nama, 
                k.tanggal_rilis, 
                s.total_play, 
                s.id_konten
            FROM 
                chart c
            JOIN 
                playlist_song ps ON c.id_playlist = ps.id_playlist
            JOIN 
                song s ON ps.id_song = s.id_konten
            JOIN 
                konten k ON s.id_konten = k.id
            JOIN 
                artist a ON s.id_artist = a.id
            JOIN 
                akun ak ON a.email_akun = ak.email
            WHERE 
                c.id_playlist = '{chart_id}'

            ORDER BY 
                s.total_play DESC;
    """)

    results = cursor.fetchall()
    judul_playlist = results[0][0]
    songs = {
        'judul_playlist': judul_playlist,
        'songs': [
                {
                    'judul': judul,
                    'artist': artist,
                    'tanggal_rilis': tanggal_rilis,  # Convert date to ISO format string
                    'total_play': total_play,
                    'id_konten': str(id_konten)  # Convert UUID to string
                }
                for _, judul, artist, tanggal_rilis, total_play, id_konten in results
            ]
    }

    print(songs)

    return render(request, "detailChart.html", songs)
