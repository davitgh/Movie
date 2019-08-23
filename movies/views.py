from django.http import HttpResponse
from django.shortcuts import render
from .models import Genre, Movie, Slider, EditorsChoice, Popular
from django.core.paginator import Paginator


def index(request):
    movies = Movie.objects.all()
    amount = len(movies)
    items = range(1, 5)

    genres = Genre.objects.all()

    paginator = Paginator(movies, 9)
    page = request.GET.get('page')
    movies = paginator.get_page(page)
    slides = Slider.objects.all()

    slider_movies = []
    for slide in slides:
        slider_movies.append(Movie.objects.get(pk=slide.slider_movies))

    popular_movies = []
    for popular in Popular.objects.all():
        popular_movies.append(Movie.objects.get(pk=popular.popular_movies))

    editors_movies = []
    for editors in EditorsChoice.objects.all():
        editors_movies.append(Movie.objects.get(pk=editors.editors_movies))
    return render(request, 'index.html', {'movies': movies, 'populars': popular_movies, 'editors_movies': editors_movies, 'genres': genres, 'amount': amount, 'slider': slider_movies})


def tv_series(request):
    genres = Genre.objects.all()
    amount = Movie.objects.all().count
    return render(request, 'tv_series.html', {'genres': genres, 'amount': amount})


def top_watched(request):
    genres = Genre.objects.all()
    amount = len(Movie.objects.all())
    return render(request, 'top_watched.html', {'genres': genres, 'amount': amount})


def top_imdb(request):
    genres = Genre.objects.all()
    amount = Movie.objects.all().count
    items = range(1, 5)
    return render(request, 'top_imdb.html', {'genres': genres, 'amount': amount, 'items': items})


def contact(request):
    genres = Genre.objects.all()
    amount = Movie.objects.all().count
    return render(request, 'contact.html', {'genres': genres, 'amount': amount})


def get_movie_by_id(request, id=1):
    genres = Genre.objects.all()
    amount = Movie.objects.all().count
    movie = Movie.objects.get(pk=id)
    return render(request, 'movie.html', {'genres': genres, 'amount': amount, 'movie': movie})

