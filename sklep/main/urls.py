from django.urls import path

from .views import ListMoviesView, RegisterView

urlpatterns = [
    path('', ListMoviesView.as_view()),
    path('register/', RegisterView.as_view()),
]