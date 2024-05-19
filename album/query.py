def get_label_album_query(email):
    return f"""
        SELECT
            STRING_AGG(al.judul, ', ') AS jumlah_judul_label,
            STRING_AGG(al.jumlah_lagu::text, ', ') AS total_lagu_label,
            STRING_AGG(al.total_durasi::text, ', ') AS jumlah_durasi_label
        FROM
            LABEL l
            LEFT JOIN ALBUM al ON l.id = al.id_label
        WHERE
            l.email = '{email}'
        GROUP BY
            l.email;
    """

def get_artist_album_query(email):
    return f"""
        SELECT
            STRING_AGG(al.judul, ', ') AS jumlah_judul_artist,
            STRING_AGG(l.nama, ', ') AS jumlah_label_artist,
            STRING_AGG(al.jumlah_lagu::text, ', ') AS total_lagu_artist,
            STRING_AGG(al.total_durasi::text, ', ') AS jumlah_durasi_artist
        FROM
            ARTIST a
            LEFT JOIN SONG so ON a.id = so.id_artist
            LEFT JOIN ALBUM al ON so.id_album = al.id
            LEFT JOIN LABEL l ON al.id_label = l.id
        WHERE
            a.email_akun = '{email}'
        GROUP BY
            a.email_akun;
    """

def get_songwriter_album_query(email):
    return f"""
        SELECT
            STRING_AGG(al.judul, ', ') AS jumlah_judul_songwriter,
            STRING_AGG(l.nama, ', ') AS jumlah_label_songwriter,
            STRING_AGG(al.jumlah_lagu::text, ', ') AS total_lagu_songwriter,
            STRING_AGG(al.total_durasi::text, ', ') AS jumlah_durasi_songwriter
        FROM
            SONGWRITER s
            LEFT JOIN SONGWRITER_WRITE_SONG sws ON s.id = sws.id_songwriter
            LEFT JOIN SONG so ON sws.id_song = so.id_konten
            LEFT JOIN ALBUM al ON so.id_album = al.id
            LEFT JOIN LABEL l ON al.id_label = l.id
        WHERE
            s.email_akun = '{email}'
        GROUP BY
            s.email_akun;
    """

def label_find_query():
    return f"""
        SELECT id, nama
        FROM LABEL;
    """

def artist_find_query():
    return f"""
        SELECT a.id, ak.nama
        FROM
            ARTIST a
            LEFT JOIN AKUN ak ON a.email_akun = ak.email;
    """

def songwriter_find_query():
    return f"""
        SELECT s.id, ak.nama
        FROM 
            SONGWRITER s
            LEFT JOIN AKUN ak ON s.email_akun = ak.email;
    """

def genre_find_query():
    return f"""
        SELECT DISTINCT genre
        FROM GENRE;
    """

def find_artist_id_hc(email):
    return f"""
        SELECT id, id_pemilik_hak_cipta
        FROM ARTIST
        WHERE email_akun = '{email}';
    """

def find_songwriter_id_hc(email):
    return f"""
        SELECT id, id_pemilik_hak_cipta
        FROM SONGWRITER
        WHERE email_akun = '{email}';
    """

def insert_album_query(id_album, judul_album, jumlah_lagu, id_label, durasi):
    return f"""
        INSERT INTO
            ALBUM (id, judul, jumlah_lagu, id_label, total_durasi)
                VALUES
                    (
                        '{id_album}',
                        '{judul_album}',
                        '{jumlah_lagu}',
                        '{id_label}',
                        '{durasi}'
                    );
    """

def insert_song_query(id_song, id_artist, id_album, play, download):
    return f"""
        INSERT INTO
            SONG (id_konten, id_artist, id_album, total_play, total_download)
                VALUES
                    (
                        '{id_song}',
                        '{id_artist}',
                        '{id_album}',
                        '{play}',
                        '{download}'
                    );
    """

def insert_royalti_query(id_phc_artist, id_song, jumlah):
    return f"""
        INSERT INTO
            ROYALTI (id_pemilik_hak_cipta, id_song, jumlah)
                VALUES
                    (
                        '{id_phc_artist}',
                        '{id_song}',
                        '{jumlah}'
                    );
    """

def insert_konten_query(id_song, judul_lagu, date_ymd, date_y, durasi):
    return f"""
        INSERT INTO
            KONTEN (id, judul, tanggal_rilis, tahun, durasi)
                VALUES
                    (
                        '{id_song}',
                        '{judul_lagu}',
                        '{date_ymd}',
                        '{date_y}',
                        '{durasi}'
                    );
    """

def insert_genre_query(id_song, genre):
    return f"""
        INSERT INTO
            GENRE (id_konten, genre)
                VALUES
                    (
                        '{id_song}',
                        '{genre}'
                    );
    """

def insert_songwriter_write_song_query(id_songwriter, id_song):
    return f"""
        INSERT INTO
            SONGWRITER_WRITE_SONG (id_songwriter, id_song)
                VALUES
                    (
                        '{id_songwriter}',
                        '{id_song}'
                    );
    """

def delete_album_query(album_name):
    return f"""
        DELETE FROM ALBUM WHERE judul = '{album_name}';
    """