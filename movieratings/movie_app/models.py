from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Rater(models.Model):
    age = models.IntegerField()
    zip = models.CharField(max_length=15)
    occupation = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.zip


class Rating(models.Model):
    rating = models.IntegerField()
    movie_rated = models.ForeignKey(Movie)
    rater = models.ForeignKey(Rater)

    def __str__(self):
        return str(self.movie_rated)