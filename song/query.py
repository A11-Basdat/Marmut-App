def get_label_song_query(email, album_name):
    return f"""
        SELECT
            STRING_AGG(k.judul, ', ') AS judul_label,
            STRING_AGG(k.durasi::text, ', ') AS durasi_label,
            STRING_AGG(so.total_play::text, ', ') AS play_label,
            STRING_AGG(so.total_download::text, ', ') AS download_label
        FROM
            Label l
            LEFT JOIN ALBUM al ON al.id_label = l.id AND al.judul = '{album_name}'
            LEFT JOIN SONG so ON so.id_album = al.id 
            LEFT JOIN KONTEN k ON so.id_konten = k.id
        WHERE
            l.email = '{email}' AND al.judul = '{album_name}'
        GROUP BY
            l.email;
    """

def get_artist_song_query(email, album_name):
    return f"""
        SELECT
            STRING_AGG(k.judul, ', ') AS judul_artist,
            STRING_AGG(k.durasi::text, ', ') AS durasi_artist,
            STRING_AGG(so.total_play::text, ', ') AS play_artist,
            STRING_AGG(so.total_download::text, ', ') AS download_artist
        FROM
            ARTIST a
            LEFT JOIN ALBUM al ON al.judul = '{album_name}'
            LEFT JOIN SONG so ON so.id_artist = a.id AND so.id_album = al.id
            LEFT JOIN KONTEN k ON so.id_konten = k.id
        WHERE
            a.email_akun = '{email}' AND al.judul = '{album_name}'
        GROUP BY
            a.email_akun;
    """

def get_songwriter_song_query(email):
    return f"""
        SELECT
            STRING_AGG(k.judul, ', ') AS judul_songwriter,
            STRING_AGG(k.durasi::text, ', ') AS durasi_songwriter,
            STRING_AGG(so.total_play::text, ', ') AS play_songwriter,
            STRING_AGG(so.total_download::text, ', ') AS download_songwriter
        FROM
            SONGWRITER s
            LEFT JOIN PEMILIK_HAK_CIPTA phc ON s.id_pemilik_hak_cipta = phc.id
            LEFT JOIN ROYALTI r ON phc.id = r.id_pemilik_hak_cipta
            LEFT JOIN SONG so ON r.id_song = so.id_konten
            LEFT JOIN KONTEN k ON so.id_konten = k.id
        WHERE
            s.email_akun = '{email}'
        GROUP BY
            s.email_akun;
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

def find_album(album_name):
    return f"""
        SELECT id
        FROM ALBUM
        WHERE judul = '{album_name}';
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