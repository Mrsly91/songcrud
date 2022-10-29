from django.db import models
from datetime import datetime

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()

    def _str_(self):
        return self.first_name


class Song(models.Model):
    artiste = models.ForeignKey(Artiste,null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    date_released = models.DateField()
    likes = models.PositveIntegerField(default=0)
    #artiste_id = models.CharField(max_length=25)
    
    def _str_(self) -> str:
        return self.title


class Lyric(models.Model):
    song = models.ForeignKey(Song, null=True, on_delete=models.CASCADE)
    content = models.TextField()
    #song_id = models.CharField(max_length=800)
    
    def _str_(self) -> str:
        return self.content
