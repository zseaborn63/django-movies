from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import ListView, DetailView
from movie_app.models import Movie, Rating


def default_view(request):
    return render_to_response(template_name='base.html', context={})

def movie_detail(request, movie_id):
    movie = Rating.objects.get(movie_rated=movie_id)
    return render_to_response(template_name='detail.html', context={"movie_object": movie})

def home_view(request):
    movies = Movie.objects.all()
    return render_to_response(template_name="movie_list.html", context={"movie_list": movies})


class MovieList(ListView):
    model = Movie


class MovieDetails(DetailView):
    model = Rating