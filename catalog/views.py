import logging

from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from catalog.models import Movie


logger = logging.getLogger('movie_logger')


def index(request):
    logger.info("Start application")
    return render(request, "base.html")


def catalog_view(request):
    movies = Movie.objects.all()
    context = {
        "movies": movies
    }
    return render(request, "movies.html", context=context)


def favourite_add(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    profile = request.user.profile_user
    if profile.favourites.filter(id=movie_id).exists():
        profile.favourites.remove(movie)
    else:
        profile.favourites.add(movie)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h3>Page not found</h3>")