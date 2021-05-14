from django.shortcuts import render

from .models import Movie

# Create your views here.

def list_movies(request):
    movies = Movie.objects.all()
    m = Movie.objects.get(id=1)
    context = {'movies': movies, 'm':m}
    return render(request, 'base.html', context)