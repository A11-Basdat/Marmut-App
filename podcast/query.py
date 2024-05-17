def get_podcast_query(podcast_id):
    return f""" 
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
    """