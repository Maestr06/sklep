from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from .forms import CommentForm, UserCreationForm
from django.http import HttpResponseRedirect, response
from django.contrib.auth import login, authenticate, forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

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

        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            resp = ''
            for i, j in form.errors.items():
                resp += str(i) + str(j) + '\n'
            print(form.error_messages)
            return response.HttpResponse('<h1>'+resp+'</h1>')
            


    def get(self, request):
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'main/register.html', context)


    



class MovieView(View):


    def get(self, request, movie_title):
        movie = Movie.objects.get(title=movie_title)
        comments = Comment.objects.filter(movie=movie.id).order_by('-posted')
        form = CommentForm()
        context = {'movie': movie, 'comments': comments, 'form': form}
        return render(request, 'main/movie.html', context)


    def post(self, request, movie_title):
        movie = Movie.objects.get(title=movie_title)
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.movie = movie
            obj.save()
            # form = CommentForm()
            # comments = Comment.objects.filter(movie=movie.id).order_by('-posted')
            # context = {'movie': movie, 'comments': comments, 'form': form}
            return HttpResponseRedirect('/movie/' + movie_title)


    
         

        







# def list_movies(request, id):
#     movies = Movie.objects.all()
#     m = Movie.objects.get(id=id)
#     context = {'movies': movies, 'm':m}
#     return render(request, 'base.html', context)