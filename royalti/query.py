def get_label_royalti_query(email):
    return f"""
        SELECT
            STRING_AGG(k.judul, ', ') AS lagu_label,
            STRING_AGG(al.judul, ', ') AS album_label,
            STRING_AGG(so.total_play::text, ', ') AS play_label,
            STRING_AGG(so.total_download::text, ', ') AS download_label,
			STRING_AGG(r.jumlah::text, ', ') AS royalti_label
        FROM
            LABEL l
            LEFT JOIN PEMILIK_HAK_CIPTA phc ON l.id_pemilik_hak_cipta = phc.id
            LEFT JOIN ROYALTI r ON phc.id = r.id_pemilik_hak_cipta
            LEFT JOIN SONG so ON r.id_song = so.id_konten
            LEFT JOIN ALBUM al ON so.id_album = al.id
            LEFT JOIN KONTEN k ON so.id_konten = k.id
        WHERE
            l.email_akun = '{email}'
        GROUP BY
            l.email_akun;
    """

def get_artist_royalti_query(email):
    return f"""
        SELECT
            STRING_AGG(k.judul, ', ') AS lagu_artist,
            STRING_AGG(al.judul, ', ') AS album_artist,
            STRING_AGG(so.total_play::text, ', ') AS play_artist,
            STRING_AGG(so.total_download::text, ', ') AS download_artist,
			STRING_AGG(r.jumlah::text, ', ') AS royalti_artist
        FROM
            ARTIST a
            LEFT JOIN PEMILIK_HAK_CIPTA phc ON a.id_pemilik_hak_cipta = phc.id
            LEFT JOIN ROYALTI r ON phc.id = r.id_pemilik_hak_cipta
            LEFT JOIN SONG so ON r.id_song = so.id_konten
            LEFT JOIN ALBUM al ON so.id_album = al.id
            LEFT JOIN KONTEN k ON so.id_konten = k.id
        WHERE
            a.email_akun = '{email}'
        GROUP BY
            a.email_akun;
    """

def get_songwriter_royalti_query(email):
    return f"""
        SELECT
            STRING_AGG(k.judul, ', ') AS lagu_songwriter,
            STRING_AGG(al.judul, ', ') AS album_songwriter,
            STRING_AGG(so.total_play::text, ', ') AS play_songwriter,
            STRING_AGG(so.total_download::text, ', ') AS download_songwriter,
			STRING_AGG(r.jumlah::text, ', ') AS royalti_songwriter
        FROM
            SONGWRITER s
            LEFT JOIN PEMILIK_HAK_CIPTA phc ON s.id_pemilik_hak_cipta = phc.id
            LEFT JOIN ROYALTI r ON phc.id = r.id_pemilik_hak_cipta
            LEFT JOIN SONG so ON r.id_song = so.id_konten
            LEFT JOIN ALBUM al ON so.id_album = al.id
            LEFT JOIN KONTEN k ON so.id_konten = k.id
        WHERE
            a.email_akun = '{email}'
        GROUP BY
            a.email_akun;
    """