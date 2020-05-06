from django.db import models
from apps.authentication.models import User


class Artist(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    biography = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, related_name='album_artist', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    release_date = models.DateField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title + " - " + self.artist


class Track(models.Model):
    artist = models.ForeignKey(Artist, related_name='track_artist', on_delete=models.CASCADE)
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    track_num = models.IntegerField()
    track_title = models.CharField(max_length=255)
    track_length = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.track_title + " - " + self.artist + " - " + self.album
