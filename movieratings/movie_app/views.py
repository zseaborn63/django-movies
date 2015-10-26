from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import ListView, DetailView
from movie_app.models import Movie, Rater, Rating


def default_view(request):
    return render_to_response(template_name='base.html', context={})

class MovieList(ListView):
    model = Movie


class MovieDetail(DetailView):
    model = Movie