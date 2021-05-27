from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from .models import Movie

# Create your views here.

class HomeView(View):


    def get(self, request):
        context = {}
        return render(request, 'main.html', context)


class RegisterView(View):
    success_url = reverse_lazy('home')

    def post(self, request):
        context = {'email': request.POST['email']}
        return render(request, 'register.html', context)

    # def get(self, request):
    #     return render(request, self.success_url, {})

# def list_movies(request, id):
#     movies = Movie.objects.all()
#     m = Movie.objects.get(id=id)
#     context = {'movies': movies, 'm':m}
#     return render(request, 'base.html', context)