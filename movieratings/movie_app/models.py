from django.db import models

# Create your models here.
from django.db.models import Avg
from numpy import split

class RatingManager(models.Manager):


    @property
    def usable_movies_for_top_20(self):
        good_movies = []
        for movie in Movie.objects.all():
            if movie.rating_set.all().values_list('rating', flat=True).count() > 20:
                good_movies.append(movie)
        return good_movies

    @property
    def top_20(self):
        return sorted(self.usable_movies_for_top_20, key=lambda x: x.new_avg_rating , reverse=True)[:20]

    @property
    def top_movies(self):
        return sorted(self.usable_movies_for_top_20, key=lambda x: x.new_avg_rating , reverse=True)[:100]


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=20)

    objects = RatingManager()


    @property
    def new_avg_rating(self):
        rating_sum = sum(self.rating_set.all().values_list('rating', flat=True))
        rating_count = self.rating_set.all().values_list('rating', flat=True).count()
        average_rating = rating_sum / rating_count
        return average_rating



    def __str__(self):
        return self.title


class Rater(models.Model):
    age = models.IntegerField()
    zip = models.CharField(max_length=15)
    occupation = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)

    @property
    def avg_movie_rating(self):
        rating_sum = sum(self.rating_set.all().values_list('rating', flat=True))
        rating_count = self.rating_set.all().values_list('rating', flat=True).count()
        average_rating = rating_sum / rating_count
        return average_rating

    @property
    def top_movies_not_seen(self):
        not_seen = []
        for movie in Movie.objects.top_movies:
            if movie not in self.rating_set.all():
                not_seen.append(movie)
        return not_seen[:5]



    def __str__(self):
        return str(self.id)


class Rating(models.Model):
    rating = models.IntegerField(choices=[(1, "Awful"), (2, "Not Bad"),  (3, "Good"), (4, "Pretty Good"), (5, "Amazing")])
    movie_rated = models.ForeignKey(Movie)
    rater = models.ForeignKey(Rater)



    def __str__(self):
        return str(self.rating)