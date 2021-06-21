import uuid
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=250)
    release = models.DateField(auto_now_add=True)
    poster = models.ImageField(default='placeholder.jpg')
    price = models.CharField(max_length=6, default='100zł')
    description = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return self.title

    def list_movies():
        movies = Movie.objects.all()#.values_list('title', flat=True)
        return movies

class Code(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.UUIDField(default=uuid.uuid4, unique=True)
    active_time = models.DurationField(default=timedelta(days=30))
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date_purchased = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.movie.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    posted = models.DateField(auto_now_add=True)
    text = models.CharField(max_length=100)


    def __str__(self):
        return self.movie.title
