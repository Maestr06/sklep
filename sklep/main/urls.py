from unicodedata import name
from django.urls import path

from .views import  HomeView, MovieView, RegisterView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('movie/<str:movie_title>/', MovieView.as_view(), name='movie'),
    # path('movie/<str:movie_title>/addcomment/', AddCommentView.as_view(), name='addcomment')
    
]