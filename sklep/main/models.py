import uuid
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=250)
    release = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Code(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.UUIDField(primary_key=True, 
    unique_for_date=timedelta(days=30), default=uuid.uuid4, 
    editable=False)
    active_time = models.DurationField(default=timedelta(days=30))
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)