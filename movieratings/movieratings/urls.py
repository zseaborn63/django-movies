"""movieratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from movie_app.views import  default_view, MovieDetail, MovieList, RaterList, RaterDetail, MovieCreateRating

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', default_view, name='default'),
    url(r'^movies/$', MovieList.as_view(), name='movie_list'),
    url(r'^movies/(?P<pk>\d+)/$', MovieDetail.as_view(), name='movie_detail'),
    url(r'^raters/$', RaterList.as_view(), name='rater_list'),
    url(r'^raters/(?P<pk>\d+)/$', RaterDetail.as_view(), name='rater_detail'),
    url(r'^create_review/$', MovieCreateRating.as_view(), name='create_rating')
]
