from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    songwriter = models.CharField(max_length=255)
    tanggal_rilis = models.DateField(auto_now_add=True)
    duration = models.IntegerField()
    tahun = models.DateField(auto_now_add=True)
    total_download = models.IntegerField()
    total_play = models.IntegerField()
    album = models.CharField(max_length=255)
