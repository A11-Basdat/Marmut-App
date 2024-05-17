from django.forms import ModelForm
from playlist.models import Playlist

class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = ["title", "description"]
