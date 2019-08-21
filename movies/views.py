from django.http import HttpResponse
from django.shortcuts import render
from .models import Genre, Movie
from django.core.paginator import Paginator


def index(request):
    movies = Movie.objects.all()
    amount = len(movies)
    items = range(1, 5)

    genres = Genre.objects.all()

    paginator = Paginator(movies, 9)
    page = request.GET.get('page')
    movies = paginator.get_page(page)

    return render(request, 'index.html', {'movies': movies, 'items': items, 'genres': genres, 'amount': amount})


def tv_series(request):
    genres = Genre.objects.all()
    return render(request, 'tv_series.html', {'genres': genres})


def top_watched(request):
    genres = Genre.objects.all()
    return render(request, 'top_watched.html', {'genres': genres})


def top_imdb(request):
    genres = Genre.objects.all()
    return render(request, 'top_imdb.html', {'genres': genres})


def contact(request):
    genres = Genre.objects.all()
    return render(request, 'contact.html', {'genres': genres})



