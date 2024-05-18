def get_label_detail_query(email):
    return f"""
        SELECT
            l.nama,
            l.email,
            l.kontak,
            STRING_AGG(a.judul, ', ') AS albums
        FROM
            LABEL l
            LEFT JOIN ALBUM a ON l.id = a.id_label
        WHERE
            l.email = '{email}'
        GROUP BY
            l.nama,
            l.email,
            l.kontak;
    """

def get_podcaster_detail_query(email):
    return f"""
        SELECT
            a.email,
            a.nama,
            CASE
                WHEN a.gender = 1 THEN 'Laki-laki'
                ELSE 'Perempuan'
            END AS user_gender,
            t.jenis_paket,
            a.tempat_lahir,
            a.tanggal_lahir,
            a.kota_asal,
            STRING_AGG(k.judul, ', ') AS podcasts
        FROM
            AKUN a
            LEFT JOIN TRANSACTION t ON a.email = t.email
            LEFT JOIN PODCASTER pr ON a.email = pr.email
            LEFT JOIN PODCAST p ON pr.email = p.email_podcaster
            LEFT JOIN KONTEN k ON p.id_konten = k.id
        WHERE
            a.email = '{email}'
        GROUP BY
            a.email,
            a.nama,
            a.gender,
            t.jenis_paket,
            a.tempat_lahir,
            a.tanggal_lahir,
            a.kota_asal;
    """

def get_artist_detail_query(email):
    return f"""
        SELECT
            a.email,
            a.nama,
            CASE
                WHEN a.gender = 1 THEN 'Laki-laki'
                ELSE 'Perempuan'
            END AS user_gender,
            t.jenis_paket,
            a.tempat_lahir,
            a.tanggal_lahir,
            a.kota_asal,
            STRING_AGG(k.judul, ', ') AS songs_artist
        FROM
            AKUN a
            LEFT JOIN TRANSACTION t ON a.email = t.email
            LEFT JOIN ARTIST ar ON a.email = ar.email_akun
            LEFT JOIN SONG s ON ar.id = s.id_artist
            LEFT JOIN KONTEN k ON s.id_konten = k.id 
        WHERE
            a.email = '{email}'
        GROUP BY
            a.email,
            a.nama,
            t.jenis_paket,
            a.gender,
            a.tempat_lahir,
            a.tanggal_lahir,
            a.kota_asal;
    """

def get_songwriter_detail_query(email):
    return f"""
        SELECT
            a.email,
            a.nama,
            CASE
                WHEN a.gender = 1 THEN 'Laki-laki'
                ELSE 'Perempuan'
            END AS user_gender,
            t.jenis_paket,
            a.tempat_lahir,
            a.tanggal_lahir,
            a.kota_asal,
            STRING_AGG(k.judul, ', ') AS songs_songwriter
        FROM
            AKUN a
            LEFT JOIN TRANSACTION t ON a.email = t.email
            LEFT JOIN SONGWRITER sr ON a.email = sr.email_akun
            LEFT JOIN SONGWRITER_WRITE_SONG srwr ON sr.id = srwr.id_songwriter
            LEFT JOIN KONTEN k ON srwr.id_song = k.id 
        WHERE
            a.email = '{email}'
        GROUP BY
            a.email,
            a.nama,
            t.jenis_paket,
            a.gender,
            a.tempat_lahir,
            a.tanggal_lahir,
            a.kota_asal;
    """

def get_penggunabiasa_detail_query(email):
    return f"""
        SELECT
            a.email,
            a.nama,
            CASE
                WHEN a.gender = 1 THEN 'Laki-laki'
                ELSE 'Perempuan'
            END AS user_gender,
            t.jenis_paket,
            a.tempat_lahir,
            a.tanggal_lahir,
            a.kota_asal,
            STRING_AGG(up.judul, ', ') AS playlists
        FROM
            AKUN a
            LEFT JOIN TRANSACTION t ON a.email = t.email
            LEFT JOIN USER_PLAYLIST up ON a.email = up.email_pembuat
        WHERE
            a.email = '{email}'
        GROUP BY
            a.email,
            a.nama,
            t.jenis_paket,
            a.gender,
            a.tempat_lahir,
            a.tanggal_lahir,
            a.kota_asal;
    """