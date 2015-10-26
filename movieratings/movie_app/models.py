from django.db import models

# Create your models here.
from django.db.models import Avg
from numpy import split


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=20)

    def make_avg_rating(self):
        avg_rating = self.rating_set.aggregate(Avg('rating'))
        return avg_rating["rating__avg"]

    avg_rating = property(make_avg_rating)

    def make_raters(self):
        raters = []
        for rating in self.rating_set.all():
            raters.append(rating.rater.id)
        raters_string = str(raters)
        return raters_string

    raters = property(make_raters)

    def num_raters(self):
        raters_num = count(self.raters)
        return raters_num

    total_raters = property(num_raters)

    def __str__(self):
        return self.title


class Rater(models.Model):
    age = models.IntegerField()
    zip = models.CharField(max_length=15)
    occupation = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)

    def make_movies(self):
        movies = []
        for movie in self.rating_set.all():
            movies.append(movie.movie_rated.title)
        return movies

    movies_rated = property(make_movies)

    def get_movie_id(self):
        movie_ids = []
        for movie in self.movies_rated:
            x = movie.id
            movie_ids.append(x)
        return movie_ids


    def __str__(self):
        return str(self.id)


class Rating(models.Model):
    rating = models.IntegerField()
    movie_rated = models.ForeignKey(Movie)
    rater = models.ForeignKey(Rater)

    def __str__(self):
        return str(self.rating)