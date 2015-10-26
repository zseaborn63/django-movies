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

    def make_top_20(self):
        avg_list = []
        for movie in self.rating_set.all():
            movie_rating = self.avg_rating
            avg_list.append((movie_rating, movie))
        avg_list = avg_list.sort()
        final_list = avg_list[0:20]
        return avg_list

    the_top_20 = property(make_top_20)

    def __str__(self):
        return self.title


class Rater(models.Model):
    age = models.IntegerField()
    zip = models.CharField(max_length=15)
    occupation = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)


    def __str__(self):
        return str(self.id)


class Rating(models.Model):
    rating = models.IntegerField()
    movie_rated = models.ForeignKey(Movie)
    rater = models.ForeignKey(Rater)

    def __str__(self):
        return str(self.rating)