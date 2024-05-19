from django.shortcuts import render
from django.db import connection
from chart.query import get_songlist_query

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
    cursor.execute(get_songlist_query(chart_id))

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

    return render(request, "detailChart.html", songs)
