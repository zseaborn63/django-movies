from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import ListView
from movie_app.models import Movie


def default_view(request):
    return HttpResponse("working")

def home_view(request):
    movies = Movie.objects.all()
    return render_to_response(template_name="home.html", context={"movie_list": movies})


class HomeView(ListView):

    model = Movie