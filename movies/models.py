from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=255)
    img_url = models.CharField(max_length=2083)
    trailer_url = models.CharField(max_length=2083)
    video_url = models.CharField(max_length=2083)
    genre = models.CharField(max_length=127)
    release_date = models.CharField(max_length=127)
    director = models.CharField(max_length=255)
    rating = models.FloatField()
    country = models.CharField(max_length=127)
    duration = models.SmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name, self.release_date


class Slider(models.Model):
    slider_movies = models.CharField(max_length=100)

    def __str__(self):
        return self.slider_movies

