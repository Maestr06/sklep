from django.contrib import admin
from .models import Movie, Code, Comment

# Register your models here.
admin.site.register(Movie)
admin.site.register(Code)
admin.site.register(Comment)
