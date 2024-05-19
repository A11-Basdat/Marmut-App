def format_podcast_data(results):
    judul, genre, nama, durasi, tanggal_rilis, tahun, *_ = results[0]
    
    jam = durasi // 60
    menit = durasi % 60
    formatted_durasi = f"{jam} Jam {menit} Menit"
    
    podcast = {
        'judul': judul,
        'genre': genre,
        'nama': nama,
        'durasi': formatted_durasi,
        'tanggal_rilis': tanggal_rilis,
        'tahun': tahun,
        'episodes': []
    }
    
    for _, _, _, _, _, _, episode_judul, deskripsi, episode_durasi, episode_tanggal_rilis in results:
        episode = {
            'episode_judul': episode_judul,
            'deskripsi': deskripsi,
            'episode_durasi': episode_durasi,
            'episode_tanggal_rilis': episode_tanggal_rilis
        }
        podcast['episodes'].append(episode)
    
    return podcast
