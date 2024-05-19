
def get_user_query(email, password):
    return f"""
        WITH user_info AS (
            SELECT
                email,
                nama,
                password,
                'akun' AS user_type
            FROM
                AKUN
            WHERE
                email = '{email}' AND password = '{password}'
            UNION ALL
            SELECT
                email,
                nama,
                password,
                'label' AS user_type
            FROM
                LABEL
            WHERE
                email = '{email}' AND password = '{password}'
        )
        SELECT
            ui.email,
            ui.nama,
            CASE
                WHEN l.email is NOT NULL THEN 'label'
                WHEN p.email IS NOT NULL THEN 'podcaster'
                WHEN ar.email_akun IS NOT NULL THEN 'artist'
                WHEN s.email_akun IS NOT NULL THEN 'songwriter'
                ELSE 'penggunabiasa'
            END AS user_role
        FROM
            user_info ui
            LEFT JOIN AKUN a ON ui.email = a.email
            LEFT JOIN LABEL l ON ui.email = l.email
            LEFT JOIN PODCASTER p ON ui.email = p.email
            LEFT JOIN ARTIST ar ON ui.email = ar.email_akun
            LEFT JOIN SONGWRITER s ON ui.email = s.email_akun
        WHERE
            ui.email = '{email}' AND ui.password = '{password}';
"""

def insert_akun_query(email, password, nama, tempat_lahir, tanggal_lahir, kota_asal, gender, role):
    if role == 'podcaster' or role == 'artist' or role == 'songwriter':
        return f"""
            INSERT INTO
            AKUN (email, password, nama, gender, tempat_lahir, tanggal_lahir, is_verified, kota_asal)
                VALUES
                    (
                        '{email}',
                        '{password}',
                        '{nama}',
                        '{gender}',
                        '{tempat_lahir}',
                        '{tanggal_lahir}',
                        'Yes',
                        '{kota_asal}'
                    );
            """
    else:
        return f"""
            INSERT INTO
            AKUN (email, password, nama, gender, tempat_lahir, tanggal_lahir, is_verified, kota_asal)
                VALUES
                    (
                        '{email}',
                        '{password}',
                        '{nama}',
                        '{gender}',
                        '{tempat_lahir}',
                        '{tanggal_lahir}',
                        'No',
                        '{kota_asal}'
                    );
            """

def insert_podcaster_query(email):
    return f"""
        INSERT INTO
        PODCASTER (email)
        VALUES
            (
                '{email}'
            );
    """

def insert_artist_query(id, email, id_phc):
    return f"""
        INSERT INTO
        ARTIST (id, email_akun, id_pemilik_hak_cipta)
        VALUES
            (
                '{id}',
                '{email}',
                '{id_phc}'
            );
    """

def insert_songwriter_query(id, email, id_phc):
    return f"""
        INSERT INTO
        SONGWRITER (id, email_akun, id_pemilik_hak_cipta)
        VALUES
            (
                '{id}',
                '{email}',
                '{id_phc}'
            );
    """

def insert_label_query(id, nama, email, password, kontak):
    return f"""
        INSERT INTO
        LABEL (id, nama, email, password, kontak)
        VALUES
            (
                '{id}',
                '{nama}',
                '{email}',
                '{password}',
                '{kontak}'
            );
    """

def insert_phc_query(id, rate_royalti):
    return f"""
        INSERT INTO
        PEMILIK_HAK_CIPTA (id, rate_royalti)
        VALUES
            (
                '{id}',
                '{rate_royalti}'
            );
    """

def check_user_query(email):
    return f"""
        WITH user_info AS (
            SELECT
                email,
                'akun' AS user_type
            FROM
                AKUN
            WHERE
                email = '{email}'
            UNION ALL
            SELECT
                email,
                'label' AS user_type
            FROM
                LABEL
            WHERE
                email = '{email}'
        )
        SELECT
            ui.email
        FROM
            user_info ui
        WHERE
            ui.email = '{email}';
"""