def get_songlist_query(chart_id):
    return f"""
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
                s.total_play DESC
            LIMIT 20;
    """