from django.shortcuts import render
from django.views import View

from .models import Movie

# Create your views here.

class ListMoviesView(View):
    

    def get(self, request):
        movies = Movie.objects.all()
        m = Movie.objects.all()
        context = {'movies': movies, 'm':m}
        return render(request, 'main.html', context)


class RegisterView(View):
    

    def post(self, request):
        context = {'email': request.POST['email']}
        return render(request, 'register.html', context)

# def list_movies(request, id):
#     movies = Movie.objects.all()
#     m = Movie.objects.get(id=id)
#     context = {'movies': movies, 'm':m}
#     return render(request, 'base.html', context)