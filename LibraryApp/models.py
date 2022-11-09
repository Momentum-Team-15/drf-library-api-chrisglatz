from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class Books(models.Model)
    title = models.CharField(max_length=200)
    author = models.Charfield(max_length=50)
    genre = models.Charfield(max_length=50)
    pubdate = models.datefield()
    is_favorite = models.BooleanField()

    def __str__(self):
        return self.title