from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from .forms import CommentForm, RegisterForm
from django.http import HttpResponseRedirect, response
from django.contrib.auth import login, authenticate

from .models import Comment, Movie

# Create your views here.

class HomeView(View):


    def get(self, request):
        movies = Movie.list_movies()
        context = {'movies1': movies}
        return render(request, 'main/main.html', context)


class RegisterView(View):
    '''class that takes care of POST/GET
    requests at /register and provides a RegisterForm'''
    success_url = reverse_lazy('home')


    def post(self, request):

        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')


    def get(self, request):
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'main/register.html', context)


class MovieView(View):


    def get(self, request, movie_title):
        movie = Movie.objects.get(title=movie_title)
        comments = Comment.objects.filter(movie=movie.id).order_by('posted')
        context = {'movie': movie, 'comments': comments}
        return render(request, 'main/movie.html', context)



class AddCommentView(View):


    def get(self, request, movie_title):

        form = CommentForm(request.GET)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/movie/' + movie_title)
        







# def list_movies(request, id):
#     movies = Movie.objects.all()
#     m = Movie.objects.get(id=id)
#     context = {'movies': movies, 'm':m}
#     return render(request, 'base.html', context)