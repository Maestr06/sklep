from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.list_movies, name='list_movies'),
]