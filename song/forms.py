from django import forms

class createSongArtistForm(forms.Form):
    def __init__(self, songwriter, genre, *args, **kwargs):
        super(createSongArtistForm, self).__init__(*args, **kwargs)
        self.fields['daftar_songwriter'].choices = songwriter
        self.fields['daftar_genre'].choices = genre

    def is_valid(self):
        valid = super().is_valid()

        if not self.cleaned_data.get('daftar_songwriter'):
            self.add_error('daftar_songwriter', 'Songwriter harus diisi')
            return False

        if not self.cleaned_data.get('daftar_genre'):
            self.add_error('daftar_genre', 'Genre harus diisi')
            return False

        return valid

    daftar_songwriter = forms.ChoiceField()
    daftar_genre = forms.ChoiceField()
    judul_lagu = forms.CharField(
        label='Judul Lagu',
        widget=forms.TextInput(attrs={'id': 'create-album-judul-lagu-artist', 'placeholder': 'Judul Lagu'}))
    durasi = forms.CharField(
        label='Durasi',
        widget=forms.TextInput(attrs={'id': 'create-album-durasi-artist', 'placeholder': 'Durasi'}))

class createAlbumSongwriterForm(forms.Form):
    def __init__(self, artist, genre, *args, **kwargs):
        super(createAlbumSongwriterForm, self).__init__(*args, **kwargs)
        self.fields['daftar_artist'].choices = artist
        self.fields['daftar_genre'].choices = genre

    def is_valid(self):
        valid = super().is_valid()

        if not self.cleaned_data.get('daftar_artist'):
            self.add_error('daftar_artist', 'Artist harus diisi')
            return False

        if not self.cleaned_data.get('daftar_genre'):
            self.add_error('daftar_genre', 'Genre harus diisi')
            return False

        return valid

    daftar_artist = forms.ChoiceField()
    daftar_genre = forms.ChoiceField()
    judul_lagu = forms.CharField(
        label='Judul Lagu',
        widget=forms.TextInput(attrs={'id': 'create-album-judul-lagu-artist', 'placeholder': 'Judul Lagu'}))
    durasi = forms.CharField(
        label='Durasi',
        widget=forms.TextInput(attrs={'id': 'create-album-durasi-artist', 'placeholder': 'Durasi'}))
