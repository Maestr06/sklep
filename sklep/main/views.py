from django.shortcuts import render

from .models import Movie

# Create your views here.

def list_movies(request, id):
    movies = Movie.objects.all()
    m = Movie.objects.get(id=id)
    context = {'movies': movies, 'm':m}
    return render(request, 'base.html', context)