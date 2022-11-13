from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint
# Create your models here.


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    pubdate = models.DateField()
    is_featured = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name="books", null=True, blank=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['title', 'author'],
                             name='unique_book_author')
        ]

    def __str__(self):
        return self.title


class Note(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='notes')
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='notes')
    date_created = models.DateTimeField(auto_now_add=True)
    note_title = models.CharField(max_length=50)
    entry = models.TextField(max_length=250)

    def __str__(self):
        return self.title
