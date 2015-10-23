
import pandas as pd
from movie_app.models import Movie, Rater


def load_movie_title(apps, schema_editor):
    movie_df = pd.read_csv("~/Desktop/Projects/django-movies/ml-100k/u.item", sep='|', encoding="ISO-8859-1", names=["Movie_ID", "Movie", "Release_Date", "blank", "IMdb_addy", "Random_nums","num", "num", "num", "num", "num", "num", "num", "num", "num", "num", "num", "num", "num", "num", "num", "num", "num", "num"])

    for row in movie_df.iterrows():
        movie_id = row[1].Movie_ID
        movie = row[1].Movie
        release_date = row[1].Release_Date
        Movie.objects.create(id=movie_id, title=movie, release_date=release_date)


def load_rater_data(apps, schema_creation):
    rater_df = pd.read_csv("~/Desktop/Projects/django-movies/ml-100k/u.user", sep='|', names=["user_id", "age", "gender","occupation", "zip"])


    for row in rater_df.iterrows():
            rater_id = row[1].user_id
            age = row[1].age
            gender = row[1].gender
            occupation = row[1].occupation
            zip = row[1].zip
            Rater.objects.create(id=rater_id, age=age, gender=gender, occupation=occupation, zip=zip)


def load_rating_data(apps, schema_editor):
    ratings_df = pd.read_csv("~/Desktop/Projects/django-movies/ml-100k/u.data", sep='\t', names=["rater", "movie", "rating","datetime"])

    Rating = apps.get_model("movie_app", "Rating")
    Movie = apps.get_model("movie_app", "Movie")
    Rater = apps.get_model("movie_app", "Rater")
    for row in ratings_df.iterrows():
            rating = row[1].rating
            movie = row[1].movie
            rater = row[1].rater
            Rating.objects.create(movie_rated=Movie.objects.get(id=movie), rater=Rater.objects.get(id=rater), rating=rating)