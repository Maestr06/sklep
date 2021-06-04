from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

from .models import Movie

# Create your views here.

class HomeView(View):

    def get(self, request):
        context = {}
        return render(request, 'main.html', context)


class RegisterView(View):
    success_url = reverse_lazy('home')


    def post(self, request):

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')


    def get(self, request):
        form = UserCreationForm()
        context = {'email': request.GET['email'], 'form': form}
        return render(request, 'register.html', context)


# def list_movies(request, id):
#     movies = Movie.objects.all()
#     m = Movie.objects.get(id=id)
#     context = {'movies': movies, 'm':m}
#     return render(request, 'base.html', context)