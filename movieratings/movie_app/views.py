from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from movie_app.models import Movie, Rater, Rating


def default_view(request):
    final_list = Movie.objects.top_20
    return render_to_response(template_name='base.html', context={"top_20": final_list})

class MovieList(ListView):
    model = Movie


class MovieDetail(DetailView):
    model = Movie
    
class RaterList(ListView):
    model = Rater
    
class RaterDetail(DetailView):
    model = Rater
    
class MovieCreateRating(CreateView):
    model = Rating
    fields = ['rater', 'movie_rated', 'rating']
    success_url = '/'