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

def trigger_durasi():
    return f""" 
        CREATE OR REPLACE FUNCTION update_durasi_podcast()
        RETURNS trigger AS
        $$
        BEGIN
        IF TG_OP = 'DELETE' THEN
        UPDATE KONTEN SET durasi = durasi - OLD.durasi WHERE id = OLD.id_konten_podcast;
        ELSIF TG_OP = 'INSERT' THEN
        UPDATE KONTEN SET durasi = durasi + NEW.durasi WHERE id = NEW.id_konten_podcast;
        END IF;
        RETURN NEW;
        END;
        $$
        LANGUAGE plpgsql;
        
        CREATE TRIGGER episode_insert_trigger
        AFTER INSERT ON EPISODE
        FOR EACH ROW EXECUTE PROCEDURE update_durasi_podcast();
        
        CREATE TRIGGER episode_delete_trigger
        AFTER DELETE ON EPISODE
        FOR EACH ROW EXECUTE PROCEDURE update_durasi_podcast();
    """