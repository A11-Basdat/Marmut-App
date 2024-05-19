from django import forms

class createAlbumArtistForm(forms.Form):
    def __init__(self, label, songwriter, genre, *args, **kwargs):
        super(createAlbumArtistForm, self).__init__(*args, **kwargs)
        self.fields['daftar_label'].choices = label
        self.fields['daftar_songwriter'].choices = songwriter
        self.fields['daftar_genre'].choices = genre

    def is_valid(self):
        valid = super().is_valid()

        if not self.cleaned_data.get('daftar_label'):
            self.add_error('daftar_label', 'Label harus diisi')
            return False

        if not self.cleaned_data.get('daftar_songwriter'):
            self.add_error('daftar_songwriter', 'Songwriter harus diisi')
            return False

        if not self.cleaned_data.get('daftar_genre'):
            self.add_error('daftar_genre', 'Genre harus diisi')
            return False

        return valid

    daftar_label = forms.ChoiceField()
    daftar_songwriter = forms.ChoiceField()
    daftar_genre = forms.ChoiceField()
    judul_album = forms.CharField(
        label='Judul Album',
        widget=forms.TextInput(attrs={'id': 'create-album-judul-album-artist', 'placeholder': 'Judul Album'}))
    judul_lagu = forms.CharField(
        label='Judul Lagu',
        widget=forms.TextInput(attrs={'id': 'create-album-judul-lagu-artist', 'placeholder': 'Judul Lagu'}))
    durasi = forms.CharField(
        label='Durasi',
        widget=forms.TextInput(attrs={'id': 'create-album-durasi-artist', 'placeholder': 'Durasi'}))

class createAlbumSongwriterForm(forms.Form):
    def __init__(self, label, artist, genre, *args, **kwargs):
        super(createAlbumSongwriterForm, self).__init__(*args, **kwargs)
        self.fields['daftar_label'].choices = label
        self.fields['daftar_artist'].choices = artist
        self.fields['daftar_genre'].choices = genre

    def is_valid(self):
        valid = super().is_valid()

        if not self.cleaned_data.get('daftar_label'):
            self.add_error('daftar_label', 'Label harus diisi')
            return False

        if not self.cleaned_data.get('daftar_artist'):
            self.add_error('daftar_artist', 'Artist harus diisi')
            return False

        if not self.cleaned_data.get('daftar_genre'):
            self.add_error('daftar_genre', 'Genre harus diisi')
            return False

        return valid

    daftar_label = forms.ChoiceField()
    daftar_artist = forms.ChoiceField()
    daftar_genre = forms.ChoiceField()
    judul_album = forms.CharField(
        label='Judul Album',
        widget=forms.TextInput(attrs={'id': 'create-album-judul-album-artist', 'placeholder': 'Judul Album'}))
    judul_lagu = forms.CharField(
        label='Judul Lagu',
        widget=forms.TextInput(attrs={'id': 'create-album-judul-lagu-artist', 'placeholder': 'Judul Lagu'}))
    durasi = forms.CharField(
        label='Durasi',
        widget=forms.TextInput(attrs={'id': 'create-album-durasi-artist', 'placeholder': 'Durasi'}))
