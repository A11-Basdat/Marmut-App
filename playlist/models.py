from django.db import models
from django.contrib.auth.models import User

class Playlist(models.Model):
    title = models.CharField(max_length=255)
    total = models.IntegerField()
    duration = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
